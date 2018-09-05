### StackOverflow - Lite
[![Build Status](https://travis-ci.org/Nduhiu17/StackOverflow-lite-v1.svg?branch=challenge-two)](https://travis-ci.org/Nduhiu17/StackOverflow-lite-v1)
[![Coverage Status](https://coveralls.io/repos/github/Nduhiu17/StackOverflow-lite-v1/badge.svg?branch=challenge-two)](https://coveralls.io/github/Nduhiu17/StackOverflow-lite-v1?branch=challenge-two)
[![Maintainability](https://api.codeclimate.com/v1/badges/f1dae9885bc88e9accb7/maintainability)](https://codeclimate.com/github/Nduhiu17/StackOverflow-lite-v1/maintainability)

#### Description
StackOverflow-lite is a platform where users can ask questions and post answers to questions.

#### Development
This Application is developed using Python datastructures with Flask restplus framework 

Please click [gh-pages](https://nduhiu17.github.io/StackOverflow-lite/) to view my UI pages

Please click [heroku-link](https://antony-stackoverflow-v1.herokuapp.com) to get and test API end points on postman

#### Features
- Users can post a question
- Users can get all questions
- Users can get a single question with its answers
- Users can post answers to questions

#### Endpoints

| METHOD | ENDPOINT                                        | DESCRIPTION                      |
| ------ | ---------------------------------------------   | -------------------------------- |
| POST   | '/api/v1/user/signup'                           | User registration                |
| POST   | '/api/v1/user/login '                           | Login signed up user             |
| POST   | '/api/v1/user/entries '                         | Create a new entry               |
| GET    | '/api/v1/user/entries/<int:entry_id>'           | Fetch a single entry             |
| GET    | '/api/v1/user/entries'                          | Fetch all entries                |
| PUT    | '/api/v1/user/entries/<int:entry_id>'           | Modify an entry                  |
| DELETE | '/api/v1/user/entries/<int:entry_id>'           | Delete an entry                  |

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

Create a start.sh file and export you app's secret key inside as shown by example_start.sh

git the file executable permissions

Run the app by:

    $ ./start.sh

Run the test by:

    $ ./test.sh