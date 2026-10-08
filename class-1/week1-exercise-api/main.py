from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from my exercise API"}

@app.get("/about")
def about():
    return {
  "name": "Week 1 Exercise API",
  "version": "1.0.0",
  "author": "your name"
}