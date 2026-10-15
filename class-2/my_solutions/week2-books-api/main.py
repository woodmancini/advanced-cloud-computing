from fastapi import FastAPI
from pathlib import Path
import sqlite3


app = FastAPI()
DB_PATH = Path(__file__).resolve().parent / "books.db"

def connect():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

@app.get("/")
def home():
    return {"message": "Books API is running"}

@app.get("/books")
def get_books():
    connection = connect()
    try: 
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * 
            FROM books
            ORDER BY id
        """)

        return [dict(row) for row in cursor.fetchall()]
    
    finally:
        connection.close()

