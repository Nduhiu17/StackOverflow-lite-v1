from flask import Flask, jsonify
from flask_restplus import Api, Resource

from app.models import Question
from app.resources import QuestionsResource,AnswerResource,QuestionResource
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

api.add_resource(QuestionsResource, '/api/v1/questions', '/api/v1/questions')
api.add_resource(QuestionResource, '/api/v1/questions/<string:id>')
api.add_resource(AnswerResource, '/api/v1/questions/<string:id>/anwsers')



@app.errorhandler(404)
#This method handles error 404
def error_404(e):
    return jsonify({"message": "The page you are looking its found.Kindly countercheck the url"}), 404


def seeding():
    # this method seeds question data
    new_question = Question(title="error sit voluptatem accusantium doloremque laudantium?",
                            body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium")
    new_question.save()


seeding()

