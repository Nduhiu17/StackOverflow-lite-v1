from flask import Flask, jsonify, Blueprint
from flask_restplus import Api

from app.models import Question, User

from config import DevelopmentConfig

authorization = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
blueprint = Blueprint('api', __name__)
blueprint_2 = Blueprint('home', __name__)

api_v1 = Api(blueprint,
             title='StackOverflow - Lite',
             version='1',
             description='An api to create a question, create an answer to a question ,get all questions and get a single '
                         'question with its answers',
             authorizations=authorization,
             )

api_home = Api(blueprint_2,
               title='StackOverflow - Lite',
               version='1',
               description='An api to create a question, create an answer to a question ,get all questions and get a single '
                           'question with its answers',
               authorizations=authorization,
               doc='/docv/',
               base_url="/"
               )

app.register_blueprint(blueprint)


@app.errorhandler(404)
# This method handles error 404
def error_404(e):
    return jsonify({"message": "Sorry!!!The page you were looking for was not found.Kindly countercheck the url"}), 404


def seeding():
    # this method seeds question data
    new_question = Question(title="error sit voluptatem accusantium doloremque laudantium?",
                            body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium")
    new_question.save()

    new_user = User(username="Nduhiumundia", email="antony@gmail.com", password="njksandknpoi20909HHKJ5522765@@")
    new_user.save_user()


seeding()

from . import views
