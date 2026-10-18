from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import sqlite3


app = FastAPI()

DB_PATH = Path(__file__).resolve().parent / "notes.db"

class NoteCreate(BaseModel):
    title: str
    text: str

class NoteUpdate(BaseModel):
    title: str | None = None
    text: str | None = None
    # text: str | None
    # this part is the type hint - it can be string or None
    # = None 
    # setting the default value

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    # by default, SQLite returns rows as standard Python tuples
    # this sets the row_factory attribute of the Connection object
    # to the Row class, which is like an optimised dictionary - access values by fieldname not index
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    text TEXT NOT NULL
)
"""        
    )
    connection.commit()
    # saves pending changes to the database
    connection.close()

create_table()

@app.get("/")
def home():
    return {"message:","Notes API is runnning"}

@app.get("/notes")
def get_notes():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM notes ORDER BY id")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        connection.close()

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM notes WHERE id = ?", (note_id,)
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        raise HTTPException(status_code=404, detail= "Note not found")

    return dict(row)

# 201 = successfully created
@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO notes (title, text) VALUES (?, ?)",
        (note.title, note.text)
    )
    connection.commit()
    note_id = cursor.lastrowid
    connection.close()
    return {"id": note_id, "title": note.title, "text": note.text}

@app.patch("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    existing = cursor.fetchone()

    if existing is None: 
        connection.close()
        raise HTTPException(status_code=404, detail="Note not found")

    new_title = note.title if note.title is not None else existing["title"]
    new_text = note.text if note.text is not None else existing["text"]

    cursor.execute(
        "UPDATE notes SET title = ?, text = ? WHERE id = ?",
        (new_title, new_text, note_id)
    )
    connection.commit()
    connection.close()

    return {"id": note_id, "title": new_title, "text": new_text}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM notes WHERE id = ?", (note_id,)
        # (note_id,) means: a tuple with one item
    )
    existing = cursor.fetchone()

    if existing is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Note not found")

    cursor.execute(
        "DELETE FROM notes WHERE id = ?", (note_id,)
        )
    connection.commit()
    connection.close()

    return {"message":"Note deleted"}