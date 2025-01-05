"""
Creddie Front-end Webserver.


FastAPI returns HTML.
"""

import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from creddie_front.routes import router

creddie_dir = pathlib.Path(__file__).parent.resolve()
templates = Jinja2Templates(directory=creddie_dir / "templates")

favicon_path = creddie_dir / 'favicon.svg'

app = FastAPI(
    version = "0.1.0",
    title = "Creddie Frontend",
    description="Frontend for a spending tracker for the future!"
)

@app.get("/", response_class=HTMLResponse)
async def index_route(req: Request):
    return templates.TemplateResponse(
        request=req, name="index.html", context={"message": "Creddie says Hello!"}
    )


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


app.include_router(router)
