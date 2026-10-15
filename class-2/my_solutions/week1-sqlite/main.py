from fastapi import FastAPI
from pathlib import Path
import sqlite3

# access the port on my local machine:
# http://127.0.0.1:8000/

app = FastAPI()

DATABASE_PATH = Path(__file__).resolve().parent / "university.db"

def get_connection():
    connection = sqlite3.connect(DATABASE_PATH) # returns a Connection object
    connection.row_factory = sqlite3.Row # packages rows into a special dictionary-like object, so you can access by column name instead of index
    return connection

@app.get("/")
def home():
    return {"message":"University API is running"}

# returns a list of dicts, which maps perfectly to a JSON
@app.get("/students")
def get_students():

    connection = get_connection()
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students ORDER BY id")
        rows = cursor.fetchall()
        # alternatively:
        # return [dict(row) for row in cursor.fetchall()]

    finally:
        connection.close()

    students = []

    for row in rows:
        students.append(dict(row))

    return students