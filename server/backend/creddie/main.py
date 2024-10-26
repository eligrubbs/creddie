"""Main for Creddie App.

"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index_route():
    return {"message": "Creddie says Hello!"}
