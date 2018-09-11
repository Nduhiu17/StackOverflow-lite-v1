import re
from datetime import datetime

from flask_restplus import Resource, reqparse, fields
from flask import request

from app import api_v1, api_home
from app.database import connect_to_db, create_answers_table, create_questions_table
from app.models import Question, Answer

cursor = connect_to_db()
create_answers_table()
create_questions_table()

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
        question = Question.save(self, title=request.json['title'], body=request.json['body'],
                                 date_created=datetime.now(), date_modified=datetime.now())
        return {"message": "The question posted successfully", "data": question}, 201

    def get(self):
        # method that gets all questions resource
        questions = Question.get_all()
        return {"message": "Success", "data": questions}, 200


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
        answer = Answer.save(self, body=request.json['body'], question_id=id, date_created=datetime.now(),
                             date_modified=datetime.now())

        return {"message": "The answer was posted successfully", "data": answer}, 201


@ns.route('/questions/<string:id>')
class QuestionResource(Resource):
    '''Class for a single question resource'''

    def get(self, id):
        # method that gets all questions resource

        question = Question.get_by_id(id)

        if question == None:
            return {"status": "No question with that id"}, 404

        return {"message": "Success", "data": question}, 200
