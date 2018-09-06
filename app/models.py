import uuid

from datetime import datetime

# create a mock database
MOCK_DATABASE = {
    "questions": [],
    "answers": [],
    "users": []

}


class Question:
    '''Class to model a question'''

    def __init__(self, title, body):
        # method to initialize Question class
        self.id = uuid.uuid4()
        self.title = title
        self.body = body
        self.date_created = datetime.now()
        self.date_modified = datetime.now()

    def json_dumps(self):
        # method to return a json object from the question details
        obj = {
            "id": str(self.id),
            "title": self.title,
            "body": self.body,
            "date_created": str(self.date_created),
            "date_modified": str(self.date_modified)
        }
        return obj

    def save(self):
        # method to save a question
        MOCK_DATABASE["questions"].append(self)
        return self.json_dumps()

    @classmethod
    def get_by_id(cls, id):
        # method to get a question by id
        retrieved_question = Question
        for item in MOCK_DATABASE['questions']:
            if str(item.id) == id:
                retrieved_question = item.json_dumps()
                answers = Answer.get_all_question_answers(question_id=id)
                retrieved_question['answers'] = answers
                return retrieved_question

    @classmethod
    def get_all(cls):
        # method to get all questions
        all_questions = MOCK_DATABASE['questions']
        get_all_json = []
        for item in all_questions:
            get_all_json.append(item.json_dumps())
        return get_all_json


class Answer:
    '''Class to model an answer'''

    def __init__(self, body, question_id):
        # method to initialize Answer class
        self.id = uuid.uuid4()
        self.body = body
        self.question_id = question_id
        self.date_created = datetime.now()
        self.date_modified = datetime.now()

    def save(self):
        # method to save an answer
        MOCK_DATABASE["answers"].append(self)
        return self.json_dumps()

    @classmethod
    def get_all_question_answers(cls, question_id):
        # method to get all answers of a given question
        all_answers = MOCK_DATABASE['answers']

        answers_retrieved = []

        for answer in all_answers:
            if answer.question_id == question_id:
                answers_retrieved.append(answer.json_dumps())
        return answers_retrieved

    def json_dumps(self):
        # method to return a json object from the answer details
        ans = {
            "id": str(self.id),
            "body": self.body,
            "question_id": self.question_id,
            "date_created": str(self.date_created),
            "date_modified": str(self.date_modified)
        }
        return ans


class User:
    '''Class to model a user'''

    def __init__(self, username, email, password):
        # method to initialize User class
        self.id = uuid.uuid4()
        self.username = username
        self.email = email
        self.password = password
        self.date_created = datetime.now()
        self.date_modified = datetime.now()

    def save_user(self):
        # method to save a user
        MOCK_DATABASE["users"].append(self)

    @classmethod
    # method to get all users
    def get_all_users(cls):
        all_users = MOCK_DATABASE['users']
        get_all_users_json = []
        for item in all_users:
            get_all_users_json.append(item.json_dumps())
        return get_all_users_json

    def json_dumps(self):
        # this method returns a user as a dict
        user = {
            "id": str(self.id),
            "username": self.username,
            "email": self.email,
            "date_created": str(self.date_created)
        }
        return user
