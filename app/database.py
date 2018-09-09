import os

import psycopg2

def connect_to_db():
    #Function to create a database connection
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    conn.autocommit = True
    cursor = conn.cursor()

    return cursor