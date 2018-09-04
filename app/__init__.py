from flask import Flask, jsonify
from flask_restplus import Api, Resource

from app.models import Question
from app.resources import QuestionsResource
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

api.add_resource(QuestionsResource, '/api/v1/questions')



@app.errorhandler(404)
#This method handles error 404
def error_404(e):
    return jsonify({"message": "The page you are looking its found.Kindly countercheck the url"}), 404



