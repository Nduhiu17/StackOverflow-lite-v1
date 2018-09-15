from datetime import datetime

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, create_access_token
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.database import connect_to_db

cursor = connect_to_db()


class Question:
    '''Class to model a question'''

    def __init__(self, id, title, body, user_id, date_created, date_modified):
        '''method to initialize Question class'''
        self.id = id
        self.title = title
        self.body = body
        self.user_id = user_id
        self.date_created = date_created
        self.date_modified = date_modified

    def json_dumps(self):
        '''method to return a json object from the question details'''
        obj = {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "user": User.find_by_id(self.user_id),
            "date_created": str(self.date_created),
            "date_modified": str(self.date_modified),
            "answers": Answer.get_all_question_answers(self.id)
        }
        return obj

    def save(self, title, body, user_id, date_created, date_modified):
        """Method to save a question"""
        format_str = f"""
         INSERT INTO public.questions (title,body,user_id,date_created,date_modified)
         VALUES ('{title}','{body}',{user_id},'{str(datetime.now())}','{str(datetime.now())}') ;
         """
        cursor.execute(format_str)

        return {
            "title": title,
            "body": body,
            "user_id": user_id,
            "date_created": str(date_created),
            "date_modified": str(date_modified)
        }

    @classmethod
    def get_by_id(cls, id):
        '''method to get a question by id'''
        cursor.execute('SELECT * FROM "public"."questions" WHERE id=%s', (id,))
        row = cursor.fetchone()
        if row == None:
            return None
        question = Question(id=row[0], title=row[1], body=row[2], user_id=row[3], date_created=row[4],
                            date_modified=row[5])

        retrieved_question = question.json_dumps()
        answers = Answer.get_all_question_answers(question_id=id)
        retrieved_question['answers'] = answers
        return retrieved_question

    @classmethod
    def get_all(cls):
        '''method to get all questions'''
        cursor.execute(
            f"SELECT * FROM public.questions")
        rows = cursor.fetchall()
        list_dict = []

        for item in rows:
            new = Question(id=item[0], title=item[1], body=item[2], user_id=item[3], date_created=item[4],
                           date_modified=item[5])
            list_dict.append(new.json_dumps())
        return list_dict

    @classmethod
    def get_all_user_questions(cls, user):
        '''method to get all questions of a given user'''
        question_owner = User.find_by_id(user)
        if question_owner:
            cursor.execute("SELECT * FROM public.questions WHERE user_id = %s", (user,))
            rows = cursor.fetchall()
            list_dict = []

            for item in rows:
                new = Question(id=item[0], title=item[1], body=item[2], user_id=item[3], date_created=item[4],
                               date_modified=item[5])
                list_dict.append(new.json_dumps())
            return list_dict
        return {"message":"No user with that id"}, 404

    @classmethod
    def delete_question(cls, id):
        '''method to delete a question'''
        try:
            cursor.execute('DELETE FROM public.questions CASCADE WHERE id = %s', (id,))
            return "successfully deleted"
        except Exception:
            return "failed"


class Answer:
    '''Class to model an answer'''

    def __init__(self, id, body, question_id, user_id, date_created, date_modified, accept):
        '''method to initialize Answer class'''
        self.id = id
        self.body = body
        self.question_id = question_id
        self.user_id = user_id
        self.date_created = datetime.now()
        self.date_modified = datetime.now()
        self.accept = accept

    def save(self, body, question_id, user_id, date_created, date_modified, accept):
        '''method to save an answer'''
        format_str = f"""INSERT INTO public.answers (body, question_id, user_id, date_created, date_modified)
                 VALUES ('{body}', {question_id}, {user_id},' {str(datetime.now())}', '{str(datetime.now())}');
                 """
        cursor.execute(format_str)
        return {
            "body": body,
            "question_id": question_id,
            "user_id": user_id,
            "accept": accept,
            "date_created": str(date_created),
            "date_modified": str(date_modified),
        }

    @classmethod
    def get_all_question_answers(cls, question_id):
        '''method to get all answers of a given question'''
        cursor.execute(
            f"SELECT * FROM public.answers")
        rows = cursor.fetchall()
        answers_retrieved_dict = []
        for answer in rows:
            if answer[2] == int(question_id):
                answer_question = Answer(id=answer[0], body=answer[1], question_id=answer[2], user_id=answer[3],
                                         date_created=answer[4],
                                         date_modified=answer[5], accept=answer[6])
                answers_retrieved_dict.append(answer_question.json_dumps())
        return answers_retrieved_dict

    @classmethod
    def get_by_id(cls, id):
        '''method to get an answer by id'''
        cursor.execute('SELECT * FROM "public"."answers" WHERE id=%s', (id,))
        row = cursor.fetchone()
        if row == None:
            return None
        answer = {
            "id": row[0],
            "body": row[1],
            "question_id": row[2],
            "user_id": row[3],
            "date_created": row[4],
            "date_modified": row[5]
        }
        retrieved_answer = answer
        return retrieved_answer

    @classmethod
    def update(cls, body, user_id, accept, id):
        """Method to update an answer"""
        format_str = f"""
         UPDATE public.answers SET body = '{body}', date_modified = '{str(datetime.now())}' WHERE id = {id};
         """

        cursor.execute(format_str)

        return {
            "id": id,
            "body": body,
            "user_id": user_id,
            "accept": accept,
            "date_modified": str(datetime.now())
        }

    @classmethod
    def accept(cls, id):
        '''method to accept an answer'''
        format_str = f"""UPDATE public.answers SET accept=true WHERE id = id;"""
        cursor.execute(format_str)

    def json_dumps(self):
        '''method to return a json object from the answer details'''
        ans = dict(id=self.id, body=self.body, question_id=self.question_id,
                   user=User.find_by_id(self.user_id), date_created=str(self.date_created),
                   date_modified=str(self.date_modified), accept=self.accept)
        return ans


class User:
    '''Class to model a user'''

    def __init__(self, id, username, email, password, date_created, date_modified):
        '''method to initialize User class'''
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.date_created = date_created
        self.date_modified = date_modified

    def save(self, username, email, password, date_created, date_modified):
        '''method to save a user'''
        format_str = f"""
                 INSERT INTO public.users (username,email,password,date_created,date_modified)
                 VALUES ('{username}','{email}','{password}','{str(datetime.now())}','{str(datetime.now())}');
                 """
        cursor.execute(format_str)
        return {
            "username": username,
            "email": email,
            "date_created": str(date_created),
            "date_modified": str(date_modified)
        }

    @classmethod
    def find_by_email(cls, email):
        '''This method gets a user using email'''
        try:
            cursor.execute("select * from users where email = %s", (email,))
            user = cursor.fetchone()
            return list(user)
        except Exception:
            return False

    @classmethod
    def find_by_username(cls, username):
        '''method to find a user by username'''
        try:
            cursor.execute("select * from users where username = %s", (username,))
            user = cursor.fetchone()
            return list(user)
        except Exception:
            return False

    @classmethod
    def find_by_id(cls, id):
        '''method to find a user by id'''
        try:
            cursor.execute("select * from users where id = %s", (id,))
            retrieved_user = list(cursor.fetchone())
            user = User(id=retrieved_user[0], username=retrieved_user[1], email=retrieved_user[2],
                        password=retrieved_user[3], date_created=retrieved_user[4], date_modified=retrieved_user[5])

            return user.json_dumps()
        except Exception:
            return False

    @staticmethod
    def generate_hash(password):
        '''method that returns a hash'''
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        '''method to verify password with the hash'''
        return pbkdf2_sha256.verify(password, hash)

    @staticmethod
    def create_token():
        '''method to generate token from username'''
        username = get_jwt_identity()
        expires = datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5)
        token = create_access_token(username, expires_delta=expires)
        return jsonify({'token': token}), 201

    def json_dumps(self):
        '''method to return a json object from a user'''
        ans = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }
        return ans
