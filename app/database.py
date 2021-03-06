import os  # import os

import psycopg2


def connect_to_db():
    '''Function to create a database connection'''
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    conn.autocommit = True
    cursor = conn.cursor()

    return cursor


def create_questions_table():
    '''function to create questions table'''
    cursor = connect_to_db()
    sql_command = """CREATE TABLE IF NOT EXISTS "public"."questions"  (
    id SERIAL ,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    date_created VARCHAR(80),
    date_modified VARCHAR(80),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id)
    REFERENCES users (id)
        )"""
    cursor.execute(sql_command)


def create_answers_table():
    '''function to create answers table'''
    cursor = connect_to_db()
    sql_command = """ CREATE TABLE IF NOT EXISTS "public"."answers"  (
            id SERIAL ,
            body VARCHAR(400) NOT NULL,
            question_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,            
            date_created VARCHAR(80),
            date_modified VARCHAR(80),
            accept BOOLEAN  default FALSE,
            PRIMARY KEY (id),
            FOREIGN KEY (question_id)
            REFERENCES questions (id),
            FOREIGN KEY (user_id)
            REFERENCES users (id)
                )"""
    cursor.execute(sql_command)


def create_users_table():
    '''function to create questions table'''
    cursor = connect_to_db()
    sql_command = """CREATE TABLE IF NOT EXISTS "public"."users"  (
    id SERIAL ,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_created VARCHAR(80),
    date_modified VARCHAR(80),
    PRIMARY KEY (id)
        )"""
    cursor.execute(sql_command)


def drop_questions_table():
    '''function to drop questions table'''
    cursor = connect_to_db()
    sql_command = """ DROP TABLE questions CASCADE;"""
    cursor.execute(sql_command)


def drop_answers_table():
    '''function to drop answers table'''
    cursor = connect_to_db()
    sql_command = """ DROP TABLE answers CASCADE;"""
    cursor.execute(sql_command)


def drop_users_table():
    '''function to drop answers table'''
    cursor = connect_to_db()
    sql_command = """ DROP TABLE users CASCADE;"""
    cursor.execute(sql_command)
