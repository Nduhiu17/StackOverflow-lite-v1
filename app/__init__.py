from flask import Flask, jsonify
from flask_restplus import Api

from app.models import Question, User
from app.resources import QuestionsResource, QuestionResource, AnswersResource, UsersResource
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

api.add_resource(QuestionsResource, '/api/v1/questions', '/api/v1/questions')
api.add_resource(QuestionResource, '/api/v1/questions/<string:id>')
api.add_resource(AnswersResource, '/api/v1/questions/<string:id>/anwsers')
api.add_resource(UsersResource, '/api/v1/users')



@app.errorhandler(404)
#This method handles error 404
def error_404(e):
    return jsonify({"message": "Sorry!!!The page you were looking for was not found.Kindly countercheck the url"}), 404


def seeding():
    # this method seeds question data
    new_question = Question(title="error sit voluptatem accusantium doloremque laudantium?",
                            body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium")
    new_question.save()

    new_user = User(username = "Nduhiumundia", email="antony@gmail.com",password="njksandknpoi20909HHKJ5522765@@")
    new_user.save_user()


seeding()

