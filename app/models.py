from datetime import datetime

# create a mock database
from app.database import connect_to_db

MOCK_DATABASE = dict(questions=[], answers=[], users=[])


cursor = connect_to_db()

class Question:
    '''Class to model a question'''

    def __init__(self,id, title, body,date_created,date_modified):
        # method to initialize Question class
        self.id = id
        self.title = title
        self.body = body
        self.date_created = date_created
        self.date_modified = date_modified

    def json_dumps(self):
        # method to return a json object from the question details
        obj = {
            "id": self.id,
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
        cursor.execute(
            f"SELECT * FROM public.questions")
        rows = cursor.fetchall()
        list_dict = []

        for item in rows:
            new = Question(id=item[0],title=item[1],body=item[2],date_created=item[3],date_modified=item[4])
            list_dict.append(new.json_dumps())
        return list_dict


class Answer:
    '''Class to model an answer'''

    def __init__(self, body, question_id):
        # method to initialize Answer class
        self.id = Answer.id_generator()
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

    @classmethod
    def id_generator(cls):
        #this method generates id for each answer
        all_answers = MOCK_DATABASE['answers']
        get_all_answers_json = []
        for item in all_answers:
            get_all_answers_json.append(item.json_dumps())
        number_of_answers = len(get_all_answers_json)
        next_id = number_of_answers + 1
        return next_id

    def json_dumps(self):
        # method to return a json object from the answer details
        ans = {
            "id": self.id,
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
        self.id = User.id_generator()
        self.username = username
        self.email = email
        self.password = password
        self.date_created    = datetime.now()
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

    @classmethod
    def id_generator(cls):
        #this method generates id for users
        all_users = MOCK_DATABASE['users']
        get_all_users_json = []
        for item in all_users:
            get_all_users_json.append(item.json_dumps())

        number_of_users = len(get_all_users_json)

        next_id = number_of_users + 1

        return next_id


    def json_dumps(self):
        # this method returns a user as a dict
        user = {
            "id": str(self.id),
            "username": self.username,
            "email": self.email,
            "date_created": str(self.date_created)
        }
        return user
