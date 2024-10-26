"""Main for Creddie App.

"""
from fastapi import FastAPI

# The version must be changed manually here.
API_VERSION = "0.1.0"

app = FastAPI(
    version = API_VERSION,
    title = "Creddie",
    description="A Spending Tracker For The Future!"
)


@app.get("/")
async def index_route():
    return {"message": "Creddie says Hello!"}
