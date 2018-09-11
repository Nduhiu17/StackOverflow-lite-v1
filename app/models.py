from datetime import datetime

from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.database import connect_to_db, create_answers_table, create_questions_table

cursor = connect_to_db()


class Question:
    '''Class to model a question'''

    def __init__(self, id, title, body, date_created, date_modified):
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

    @staticmethod
    def save(self, title, body, date_created, date_modified):
        """Method to save an entry"""
        format_str = f"""
         INSERT INTO public.questions (title,body,date_created,date_modified)
         VALUES ('{title}','{body}','{str(datetime.now())}','{str(datetime.now())}') ;
         """
        cursor.execute(format_str)

        return {
            "title": title,
            "body": body,
            "date_created": str(date_created),
            "date_modified": str(date_modified)
        }

    @classmethod
    def get_by_id(cls, id):
        cursor.execute('SELECT * FROM "public"."questions" WHERE id=%s', (id,))
        row = cursor.fetchone()
        if row == None:
            return None
        question = {
            "id": row[0],
            "title": row[1],
            "body": row[2],
            "date_created": row[3],
            "date_modified": row[4],
        }
        retrieved_question = question
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
            new = Question(id=item[0], title=item[1], body=item[2], date_created=item[3], date_modified=item[4])
            list_dict.append(new.json_dumps())
        return list_dict


class Answer:
    '''Class to model an answer'''

    def __init__(self, id, body, question_id, date_created, date_modified):
        # method to initialize Answer class
        self.id = id
        self.body = body
        self.question_id = question_id
        self.date_created = datetime.now()
        self.date_modified = datetime.now()

    def save(self, body, date_created, date_modified, question_id):
        # method to save an answer
        format_str = f"""
                 INSERT INTO public.answers (body,question_id,date_created,date_modified)
                 VALUES ('{body}',{question_id},'{str(datetime.now())}','{str(datetime.now())}');
                 """
        cursor.execute(format_str)
        return {
            "body": body,
            "question_id": question_id,
            "date_created": str(date_created),
            "date_modified": str(date_modified)
        }

    @classmethod
    def get_all_question_answers(cls, question_id):
        cursor.execute(
            f"SELECT * FROM public.answers")
        rows = cursor.fetchall()
        answers_retrieved_dict = []
        for answer in rows:
            if answer[2] == int(question_id):
                answer_question = Answer(id=answer[0], body=answer[1], question_id=answer[2], date_created=answer[3],
                                         date_modified=answer[4])
                answers_retrieved_dict.append(answer_question.json_dumps())
        return answers_retrieved_dict

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

    def __init__(self, username, email, password, date_created, date_modified):
        # method to initialize User class
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.date_created = date_created
        self.date_modified = date_modified

    def save(self, username, email, password, date_created, date_modified):
        # method to save a user
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
    # This method gets a user using email
    def find_by_email(cls, email):
        try:
            cursor.execute("select * from users where email = %s", (email,))
            user = cursor.fetchone()
            return list(user)
        except Exception as e:
            return False

    @classmethod
    def find_by_username(cls, username):
        try:
            cursor.execute("select * from users where username = %s", (username,))
            user = cursor.fetchone()
            return list(user)
        except Exception as e:
            return False

    @classmethod
    def find_by_id(cls, id):
        try:
            cursor.execute("select * from users where id = %s", (id,))
            user = cursor.fetchone()
            return list(user)
        except Exception as e:
            return False

    @staticmethod
    def generate_hash(password):
        #method that returns a hash
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        #method to verify password with the hash
        return pbkdf2_sha256.verify(password, hash)