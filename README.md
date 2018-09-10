### StackOverflow - Lite
[![Build Status](https://travis-ci.org/Nduhiu17/StackOverflow-lite-v1.svg?branch=develop)](https://travis-ci.org/Nduhiu17/StackOverflow-lite-v1)
[![Coverage Status](https://coveralls.io/repos/github/Nduhiu17/StackOverflow-lite-v1/badge.svg?branch=develop)](https://coveralls.io/github/Nduhiu17/StackOverflow-lite-v1?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/f1dae9885bc88e9accb7/maintainability)](https://codeclimate.com/github/Nduhiu17/StackOverflow-lite-v1/maintainability)

#### Description
StackOverflow-lite is a platform where users can ask questions and post answers to questions.

#### Development
This Application is developed using Python datastructures with Flask restplus framework 

Please click [gh-pages](https://nduhiu17.github.io/StackOverflow-lite/) to view my UI pages

Please click [heroku-link](https://antony-stackoverflow-v1.herokuapp.com) to get and test API end points on postman

Please click [code on git hub](https://github.com/Nduhiu17/StackOverflow-lite-v1/tree/challenge-two) to get the code on git hub

#### Features
- Users can post a question
- Users can get all questions
- Users can get a single question with its answers
- Users can post answers to questions

#### Endpoints

| METHOD | ENDPOINT                                            | DESCRIPTION                         |
| ------ | ---------------------------------------------       | --------------------------------    |
| POST   | '/api/v1/users/'                                    | User registration                   |
| POST   | '/api/v1/user/questions '                           | Create a new question               |
| POST   | '/api/v1/user/questions/<int:question_id>/answers'  | Create a new answer to a question   |
| GET    | '/api/v1/user/questions/<int:question_id>'          | Fetch a single question             |
| GET    | '/api/v1/user/questions'                            | Fetch all questions                 |
| GET    | '/api/v1/user/users'                                | Fetch all users - Admin             |

#### Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python web microframework)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)
- [Pylint](https://www.pylint.org/) (Linting library)
- [Pip3](https://pypi.org/project/pip/) (Python package installer)

#### Getting Started:

**To start the app, please follow the instructions below:**

**On your terminal:**

Install pip:

  $ sudo apt-get install python-pip

Clone this repository:

  $ git clone https://github.com/Nduhiu17/StackOverflow-lite-v1.git

Get into the root directory:

  $ cd StackOverflow-lite-v1/

Install virtual enviroment:

  $ python3.6 -m venv virtual

Activate the virtual environment:

  $ source virtual/bin/activate
  
Install requirements

  $ pip install -r requirements.txt

Create a start.sh file and export your app's secret key inside as shown by example_start.sh

Give the file executable permissions by right clicking the file and checking the execute button as shown by the image below:

![start](https://user-images.githubusercontent.com/30591881/45145592-b6e7fd80-b1c9-11e8-8966-4c9ae39c6f4b.png)

Run the app by:

    $ ./start.sh

#### Running the tests

Export your secret key in your test.sh file.

Give your test.sh file executable permissions as shown by the image below:

![test](https://user-images.githubusercontent.com/30591881/45145872-5d340300-b1ca-11e8-873a-fe9d9f5c4874.png)

Run the tests by:

    $ ./test.sh
