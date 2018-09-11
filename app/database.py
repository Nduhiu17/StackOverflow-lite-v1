import os

import psycopg2


def connect_to_db():
    # Function to create a database connection
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    conn.autocommit = True
    cursor = conn.cursor()

    return cursor


# function to create questions table
def create_questions_table():
    cursor = connect_to_db()
    sql_command = """CREATE TABLE IF NOT EXISTS "public"."questions"  (
    id SERIAL ,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    date_created VARCHAR(80),
    date_modified VARCHAR(80),
    PRIMARY KEY (id)
        )"""
    cursor.execute(sql_command)


# function to create answers table
def create_answers_table():
    cursor = connect_to_db()
    sql_command = """ CREATE TABLE IF NOT EXISTS "public"."answers"  (
            id SERIAL ,
            body VARCHAR(400) NOT NULL,
            question_id INTEGER NOT NULL,
            date_created VARCHAR(80),
            date_modified VARCHAR(80),
            PRIMARY KEY (id),
            FOREIGN KEY (question_id)
            REFERENCES questions (id)
                )"""
    cursor.execute(sql_command)


# function to drop questions table
def drop_questions_table():
    cursor = connect_to_db()
    sql_command = """ 
    DROP TABLE questions CASCADE;
    """
    cursor.execute(sql_command)


# function to drop answers table
def drop_answers_table():
    cursor = connect_to_db()
    sql_command = """ 
    DROP TABLE answers CASCADE;
    """
    cursor.execute(sql_command)
