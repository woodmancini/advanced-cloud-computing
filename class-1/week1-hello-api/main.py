from fastapi import FastAPI

# Import the movies router from routers/movies.py.
from routers import movies

app = FastAPI()

# Connect all routes from movies.py under the /movies URL prefix.
app.include_router(movies.router, prefix="/movies")


# Keep the home endpoint in main.py.
@app.get("/")
def home():
    return {"message": "Hello world!"}


@app.get("/hello")
def hello():
    return {"message": "world!"}