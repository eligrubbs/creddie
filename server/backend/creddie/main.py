"""Main for Creddie App.

"""
from fastapi import FastAPI

from .consts import API_VERSION


app = FastAPI(
    version = API_VERSION,
    title = "Creddie",
    description="A Spending Tracker For The Future!"
)


@app.get("/")
async def index_route():
    return {"message": "Creddie says Hello!"}
