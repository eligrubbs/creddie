"""Main for Creddie App.

"""
from fastapi import FastAPI, Request

from .api.v1.router import api_router
from .consts import API_VERSION, API_V1_STR


app = FastAPI(
    version = API_VERSION,
    title = "Creddie",
    description="A Spending Tracker For The Future!"
)


@app.get("/")
async def index_route(req: Request):
    return {"message": "Creddie says Hello!"}


app.include_router(api_router, prefix=API_V1_STR)
