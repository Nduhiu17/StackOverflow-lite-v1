import re  # import regex module

from app.database import connect_to_db
from app.models import Answer

cursor = connect_to_db()

class Validate:
    '''Class for validating data input'''

    @staticmethod
    def validate_username_format(username):
        '''method to validate a username'''
        regex = r"^[1-9]\d*(\.\d+)?$"
        if re.match(regex, username):
            return True
        return False

    @staticmethod
    def validate_length_username(username):
        '''checking the username length no be not less than 6 characters'''
        if len(username) < 4:
            return False
        return True

    @staticmethod
    def validate_password_length(password):
        '''checking password length to be not less than 5 characters'''
        if len(password) < 6:
            return False
        return True

    @staticmethod
    def validate_email_format(email):
        '''checks correct email format'''
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(regex, email, re.IGNORECASE):
            return True
        return False

    @staticmethod
    def is_question_exist(body):
        '''check if question exists'''
        query = ("""SELECT * FROM questions where body = '{}'""".format(body))
        cursor.execute(query)
        body = cursor.fetchone()
        if body:
            return True
        return False

    @staticmethod
    def check_answer_accepted(question_id):
        '''Method to check whether a question has an accepted answer'''
        answers = Answer.get_all_question_answers(question_id)
        for answer in answers:
            if answer['accept']:
                return True
        return False
