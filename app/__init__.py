from flask import Flask, jsonify, render_template, Blueprint
from flask_restplus import Api, Resource, apidoc, fields

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
api = Api(app)
blueprint = Blueprint('api', __name__, url_prefix='/api')
# api = Api(blueprint, doc='/doc/')

api = Api(blueprint,
          title='StackOverflow - Lite',
          version='1',
          description='An api to create a question, create an answer to a question ,get all questions and get a single '
                      'question with its answers',
          authorizations=authorization,
          doc='/doc/'
          )



def swagger_ui():
    return apidoc.ui_for(api)


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
