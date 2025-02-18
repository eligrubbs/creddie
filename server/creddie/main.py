import pathlib
import os
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates

from .config import settings
from .consts import CATEGORIES
from .schemas.transaction_schema import CreateTransaction


creddie_dir = pathlib.Path(__file__).parent.resolve()
templates = Jinja2Templates(directory = (creddie_dir / "templates") )


app = FastAPI(
    version = "0.0.1",
    title = "Creddie",
    description = "Financial Tracker",
)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    the_path = creddie_dir / 'favicon.ico'
    print(the_path)
    return FileResponse(the_path)


@app.get("/")
async def index_route(req: Request) -> JSONResponse:
    content = {"message": "Creddie says Hello!"}
    return JSONResponse(content = content)


@app.get("/form")
async def form_route(req: Request, key: str):
    if key != settings.FORM_ACCESS_KEY:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized to use this form")

    return templates.TemplateResponse(
        request=req, name="form.html", context = {"categories": CATEGORIES} 
    )


@app.post("/log_transaction", response_model=CreateTransaction, status_code=status.HTTP_200_OK)
async def log_transaction(req: CreateTransaction, key: str):
    if key != settings.FORM_ACCESS_KEY:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized to use this form")

    data = req.model_dump()
    with open(settings.csv_abs_path(), 'a') as csvfile:
        writer = CreateTransaction.CSVDictWriter(f=csvfile)
        # for saftey, if the csv dissapears while still up, make a new one
        if (os.stat(settings.csv_abs_path()).st_size == 0):
            writer.writeheader()
        writer.writerow(data)
    print(req.model_dump())

    return req
