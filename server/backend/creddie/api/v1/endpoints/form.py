import pathlib
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

dir_to_templates = pathlib.Path(__file__).parent.parent.parent.parent.resolve()
templates = Jinja2Templates(directory=dir_to_templates / "templates")


router = APIRouter()


@router.get("/")
def get_form_html(req: Request):

    return templates.TemplateResponse(
        request=req, name="form.html", context = {}
    )
