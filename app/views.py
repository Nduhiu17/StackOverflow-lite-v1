import re
from datetime import datetime

from flask_jwt_extended import create_access_token, jwt_required, \
    get_jwt_identity
from flask_restplus import Resource, reqparse, fields
from flask import request

from app import api_v1, api_home
from app.database import connect_to_db, create_answers_table, \
    create_questions_table, create_users_table
from app.models import Question, Answer, User
from app.validators import Validate

cursor = connect_to_db()
create_users_table()
create_questions_table()
create_answers_table()

api_v1.namespaces.clear()
ns1 = api_v1.namespace('api/v1/auth',
                       description='End points regarding user operations')
ns = api_v1.namespace('api/v1',
                      description='End points regarding questions operations')
ns3 = api_v1.namespace('api/v1',
                       description='End points regarding answers operations')
ns2 = api_home.namespace('',
                         description='Posting a question and getting all questions')
ns4 = api_v1.namespace('api/v1',
                       description='End points regarding an answer operations')


resource_fields = api_v1.model('Question', {
    'title': fields.String,
    'body': fields.String,
})


@ns.route('/questions')
class QuestionsResource(Resource):
    '''Questions class resource'''

    @ns.expect(resource_fields)
    @ns.doc(security='apiKey')
    @jwt_required
    def post(self):
        '''Create a question'''
        parser = reqparse.RequestParser()
        parser.add_argument('title', help='The title field cannot be blank',
                            required=True, type=str)
        parser.add_argument('body', help='The body field cannot be blank',
                            required=True, type=str)
        data = parser.parse_args()
        search_keys = ("title", "body")
        if all(key in data.keys() for key in search_keys):
            body = data.get("body").strip()
            does_qstn_exist = Validate.is_question_exist(body)
            if does_qstn_exist:
                return ({"message": "Question already exists, check it out for an answer"}), 409
            if re.match(r"^[1-9]\d*(\.\d+)?$", data['title']):
                return {'message': 'the title should be of type string'}, 400
            if len(data['title']) < 10:
                return {'message': 'The length of the title should be atleast 10 characters'}, 400
            if len(data['body']) < 20:
                return {'message': 'The length of your question content should be atleast 15 characters'}, 400

            question = Question.save(self, title=request.json['title'],
                                     body=request.json['body'],
                                     user_id=get_jwt_identity(),
                                     date_created=datetime.now(),
                                     date_modified=datetime.now())
            return {"message": "The question posted successfully",
                    "data": question}, 201

    def get(self):
        '''Get all questions'''
        questions = Question.get_all()
        return {"message": "Success", "data": questions}, 200





new_answer = api_v1.model('Answer', {
    'body': fields.String
})


@ns3.route('/questions/<string:id>/answers')
class AnswersResource(Resource):
    '''Answers class resource'''

    @api_v1.expect(new_answer)
    @ns.doc(security='apiKey')
    @jwt_required
    def post(self, id):
        '''Post an answer to a question'''
        parser = reqparse.RequestParser()
        parser.add_argument('body', help='The body field cannot be blank',
                            required=True, type=str)
        data = parser.parse_args()
        if len(data['body']) < 15:
            return {'message': 'Ops!,the answer is too short,kindly provide an answer of more than 15 characters'}, 400
        question_to_answer = Question.get_by_id(id)
        if question_to_answer == None:
            return {'message': 'The question with that id was not found'}, 404
        answer = Answer.save(self, body=request.json['body'], question_id=id,
                             user_id=get_jwt_identity(),
                             date_created=datetime.now(),
                             date_modified=datetime.now(), accept=False)

        return {"message": "The answer was posted successfully",
                "data": answer}, 201


@ns.route('/questions/<string:id>')
class QuestionResource(Resource):
    '''Class for a single question resource'''

    def get(self, id):
        '''Get a question by id'''

        question = Question.get_by_id(id)

        if question == None:
            return {"status": "No question found with that id"}, 404

        return {"message": "Success", "data": question}, 200

    @ns.doc(security='apiKey')
    @jwt_required
    def delete(self, id):
        '''Delete a question'''
        question_to_delete = Question.get_by_id(id)
        logged_in_user = get_jwt_identity()
        if question_to_delete:
            if question_to_delete['user']["id"] == logged_in_user:
                Question.delete_question(id)
                return {"message": "Successfully deleted"}, 200
            return {"message": "You are not authorized to delete this question"}, 401
        return {"message": "No question found"}, 404


new_user = api_v1.model('Register', {
    'username': fields.String,
    'email': fields.String,
    'password': fields.String
})


@ns1.route('/signup')
class RegisterResource(Resource):
    '''Users registration resource'''

    @api_v1.expect(new_user)
    def post(self):
        '''method that saves a user resource'''
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            help='The username field cannot be blank',
                            required=True, type=str)
        parser.add_argument('email', help='The email field cannot be blank',
                            required=True, type=str)
        parser.add_argument('password',
                            help='The password field cannot be blank',
                            required=True, type=str)
        data = parser.parse_args()
        if Validate.validate_username_format(data['username']):
            return {'message': 'Invalid username username should be of form "username"'}, 400
        if not Validate.validate_length_username(data['username']):
            return {'message': 'The length of username should be atleast 4 characters'}, 400
        if not Validate.validate_password_length(data['password']):
            return {'message': 'the length of the password should be atleast 6 characters'}, 400
        if re.match(r"^[1-9]\d*(\.\d+)?$", data['password']):
            return {'message': 'the username and password should be of type string'}, 400
        if not Validate.validate_email_format(data['email']):
            return {'message': 'Invalid email.The email should be of type "example@mail.com"'}, 400
        if User.find_by_username(data['username']):
            return {'message': 'This username is already taken,kindly try another username'}, 409
        if User.find_by_email(data['email']):
            return {'message': 'This email is already taken'}, 409

        user = User.save(self, username=request.json['username'],
                         email=request.json['email'],
                         password=User.generate_hash(request.json['password']),
                         date_created=datetime.now(),
                         date_modified=datetime.now())
        return {"message": "The user signed up successfully", "data": user}, 201


n_user = api_v1.model('Login', {
    'username': fields.String,
    'password': fields.String
})


@ns1.route('/login')
class LoginResource(Resource):
    '''Class for login resource'''

    @api_v1.expect(n_user)
    def post(self):
        ''' Login with registered details'''
        parser = reqparse.RequestParser()
        parser.add_argument('password', help='This3 field cannot be blank',
                            required=True)
        parser.add_argument('username', help='This field cannot be blank',
                            required=True)
        data = parser.parse_args()
        current_user = User.find_by_username(data['username'])
        if current_user == False:
            return {'message': 'User {} doesnt exist'.format(
                data['username'])}, 404

        if User.verify_hash(data['password'], current_user[3]):
            access_token = create_access_token(current_user[0])
            return dict(message='Logged in as {}'.format(current_user[1]),
                        access_token=access_token), 200
        return {'message': 'Wrong credentials'}, 403


@ns4.route('/questions/<string:id>/answers/<answer_id>')
class AnswerResource(Resource):
    """Class resource to update an answer"""

    @api_v1.expect(new_answer)
    @ns.doc(security='apiKey')
    @jwt_required
    def put(self, id, answer_id):
        '''Accept an answer and update an answer'''
        question = Question.get_by_id(id=id)
        logged_in_user = get_jwt_identity()
        answer_to_update = Answer.get_by_id(answer_id)
        print(answer_to_update)
        if question:
            if answer_to_update:
                if answer_to_update['user_id'] == logged_in_user:
                    parser = reqparse.RequestParser()
                    parser.add_argument('body',
                                        help='The body field cannot be blank',
                                        required=True, type=str)
                    parser.parse_args()
                    answer_to_update = Answer.update(id=answer_id,
                                                     body=request.json['body'],
                                                     user_id=get_jwt_identity(),
                                                     accept=False)
                    return {"message": "You have successfully updated the answer",
                            "data": answer_to_update}, 201
                if question['user']["id"]== logged_in_user and answer_to_update['question_id'] == question["id"]:
                    if Validate.check_answer_accepted(question_id=question["id"]):
                        return {"message": "The question has an already acceped answer"}, 405
                    Answer.accept(id=answer_id)
                    return {"message": "You have successfully accepted the answer"}, 201
                else:
                    return {"message": "You are not authorized to modify the answer"}, 401
            return {"message": "Answer not found"}, 404
        return {"message": "No question found with that answer"}, 404
