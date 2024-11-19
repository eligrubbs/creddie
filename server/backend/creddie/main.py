"""Main for Creddie App.

"""
import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from .api.v1.router import api_router
from .consts import API_VERSION, API_V1_STR


creddie_dir = pathlib.Path(__file__).parent.resolve()
templates = Jinja2Templates(directory=creddie_dir / "templates")

app = FastAPI(
    version = API_VERSION,
    title = "Creddie",
    description="A Spending Tracker For The Future!"
)

favicon_path = creddie_dir / 'favicon.svg'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/", response_class=HTMLResponse)
async def index_route(req: Request):
    return templates.TemplateResponse(
        request=req, name="index.html", context={"message": "Creddie says Hello!"}
    )


app.include_router(api_router, prefix=API_V1_STR)
