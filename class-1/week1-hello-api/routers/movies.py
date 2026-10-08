from fastapi import APIRouter, HTTPException

router = APIRouter()

# This dictionary is temporary in-memory data.
# Next week we will replace this style with SQL database data.
movies = {
    "hobbit": {
        "title": "The Hobbit",
        "description": "A fantasy adventure film based on J.R.R. Tolkien's novel.",
        "year": 2012
    },
    "matrix": {
        "title": "The Matrix",
        "description": "A science fiction film about simulated reality.",
        "year": 1999
    }
}


@router.get("/")
def get_movies():
    # Return all movie records.
    return movies


@router.get("/{movie_id}")
def get_movie(movie_id: str):
    # .get() returns None instead of crashing if the key does not exist.
    movie = movies.get(movie_id)

    if movie is None:
        # Return a clear 404 response when the movie is missing.
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie