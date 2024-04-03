from typing_extensions import Annotated

from fastapi import APIRouter, Request, Form
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import testData
from testData import clientsList

router = APIRouter(tags=["Client"])
templates = Jinja2Templates(directory="client/templates")


@router.get("/client")
def getClients(req: Request):
    return templates.TemplateResponse(
        "СlientsForm.html", context={"request": req, "client_list": clientsList}
    )


@router.get("/client/add")
def addClient(req: Request):
    return templates.TemplateResponse("addClientForm.html", context={"request": req})


@router.post("/client/add")
def addClient(
    req: Request,
    fio: Annotated[str, Form()],
    birthday: Annotated[str, Form()],
    phoneNumber: Annotated[str, Form()],
):
    clientsList.append(
        {
            "id": int(max(testData.productsList, key=lambda x: x["id"])["id"]) + 1,
            "birthday": birthday,
            "fio": fio,
            "phone_number": phoneNumber,
        }
    )
    return RedirectResponse(url="/client", status_code=status.HTTP_303_SEE_OTHER)
