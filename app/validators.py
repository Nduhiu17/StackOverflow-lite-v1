import re


class Validate:
    '''Class for validating data input'''

    @staticmethod
    def validate_username_format(username):
        regex = "^[1-9]\d*(\.\d+)?$"
        if re.match(regex,username):
            return True
        return False

    @staticmethod
    def validate_length_username(username):
        #checking the username length no be not less than 6 characters
        if len(username) < 6:
            return False
        return True

    @staticmethod
    def validate_password_length(password):
        #checking password length to be not less than 5 characters
        if len(password) < 6:
            return False
        return True

    @staticmethod
    def validate_email(email):
        #checks correct email format
        regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(regex, email, re.IGNORECASE):
            return True
        else:
            return False

    @staticmethod
    def validate_int(value):
        #check whether the value supplied is an integer
        try:
            int(value)
            return True
        except ValueError:
            return False

