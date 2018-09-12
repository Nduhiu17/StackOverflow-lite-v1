from flask import Flask, jsonify, Blueprint
from flask_restplus import Api

from config import DevelopmentConfig
from flask_jwt_extended import JWTManager

authorization = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


app = Flask(__name__)
jwt = JWTManager(app)
app.config.from_object(DevelopmentConfig)
blueprint = Blueprint('api', __name__)
blueprint_2 = Blueprint('home', __name__)
blueprint_3 = Blueprint('auth', __name__)

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


from . import views
