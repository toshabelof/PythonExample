from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(tags=["Statistics"])
templates = Jinja2Templates(directory="templates")


@router.get("/")
def get_statistics(req: Request):
    return templates.TemplateResponse(
        "StatisticsForm.html", context={"request": req}
    )