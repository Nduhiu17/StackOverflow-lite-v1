import re

from flask_restplus import Resource, reqparse, fields
from flask import request

from app import api_v1, api_home
from app.models import Question, Answer, User

api_v1.namespaces.clear()
ns = api_v1.namespace('api/v1', description='End points for the api')
ns2 = api_home.namespace('', description='Posting a question and getting all questions')

resource_fields = api_v1.model('Question', {
    'title': fields.String,
    'body': fields.String,
})


@ns.route('/questions')
class QuestionsResource(Resource):
    '''Questions class resource'''

    @ns.expect(resource_fields)
    def post(self):
        # method that post a question resource
        parser = reqparse.RequestParser()
        parser.add_argument('title', help='The title field cannot be blank', required=True, type=str)
        parser.add_argument('body', help='The body field cannot be blank', required=True, type=str)
        data = parser.parse_args()
        json_data = request.get_json(force=True)
        if re.match("^[1-9]\d*(\.\d+)?$", data['title']):
            return {'message': 'the title should be of type string'}, 400
        if len(data['title']) < 10:
            return {'message': 'The length of both title should be atleast 10 characters'}, 400
        if len(data['body']) < 20:
            return {'message': 'The length of both body should be atleast 15 characters'}, 400
        question = Question(title=request.json['title'], body=request.json['body'])
        print(type(data['title']))
        saved_question = question.save()
        return {"message": "The question posted successfully", "data": saved_question}, 201

    def get(self):
        # method that gets all questions resource
        questions = Question.get_all()
        return {"message": "200", "data": questions}, 200


new_answer = api_v1.model('Answer', {
    'body': fields.String
})


@ns.route('/questions/<string:id>/anwsers')
class AnswersResource(Resource):
    '''Answers class resource'''

    @api_v1.expect(new_answer)
    def post(self, id):
        # method that post a question resource
        parser = reqparse.RequestParser()
        parser.add_argument('body', help='The body field cannot be blank', required=True, type=str)
        data = parser.parse_args()
        json_data = request.get_json(force=True)
        if len(data['body']) < 15:
            return {'message': 'Ops!,the answer is too short,kindly provide an answer of more than 15 characters'}, 400
        question_to_answer = Question.get_by_id(id)
        if question_to_answer == None:
            return {'message': 'The question with that id was not found'}, 404
        answer = Answer(body=request.json['body'], question_id=id)
        saved_answer = answer.save()
        return {"message": "The answer was posted successfully", "data": saved_answer}, 201


@ns.route('/questions/<string:id>')
class QuestionResource(Resource):
    '''Class for a single question resource'''

    def get(self, id):
        # method that gets all questions resource

        question = Question.get_by_id(id)

        if question == None:
            return {"status": "No question with that id"}, 404

        return {"message": "Success", "data": question}, 200


new_user = api_v1.model('User', {
    'username': fields.String,
    'email': fields.String,
    'password': fields.String
})


@ns.route('/users')
class UsersResource(Resource):
    '''Users registration resource'''

    @api_v1.expect(new_user)
    def post(self):
        # method that saves a user resource
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='The username field cannot be blank', required=True, type=str)
        parser.add_argument('email', help='The email field cannot be blank', required=True, type=str)
        parser.add_argument('password', help='The password field cannot be blank', required=True, type=str)
        data = parser.parse_args()
        json_data = request.get_json(force=True)
        if len(data['username']) < 8:
            return {'message': 'The length of username should be atleast 8 characters'}, 400
        user = User(username=request.json['username'], email=request.json['email'],
                    password=request.json['password'])
        user.save_user()
        user = user.json_dumps()
        return {"message": "The user saved successfully", "data": user}, 201

    def get(self):
        # method that gets all users resource
        users = User.get_all_users()
        return {"message": "Success", "data": users}, 200
