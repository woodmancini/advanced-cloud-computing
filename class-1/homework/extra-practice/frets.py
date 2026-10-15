# URL below:
# http://127.0.0.1:8000/

from fastapi import FastAPI
from routers import instruments

app = FastAPI()

app.include_router(instruments.router, prefix="/instruments")

@app.get("/")
def home():
    return {
        "name":"Fretted instruments scale lengths",
        "version":"1.0",
        "endpoints":{
            "root":"GET /",
            "mandolin":"GET /mandolin",
            "cello":"GET /cello"
        }
    }