from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from models.client import ClientModel

router = APIRouter(tags=["Client"])
templates = Jinja2Templates(directory="templates")


@router.get("/clients")
def get_clients(req: Request):
    clients = ClientModel.get_clients()
    return templates.TemplateResponse(
        "ClientsForm.html", context={"request": req, "client_list": clients}
    )


@router.get("/clients/add")
def add_client(req: Request):
    return templates.TemplateResponse("AddClientForm.html", context={"request": req})
#
#
# @router.post("/client/add")
# def addClient(
#     req: Request,
#     fio: Annotated[str, Form()],
#     birthday: Annotated[str, Form()],
#     phoneNumber: Annotated[str, Form()],
# ):
#     clientsList.append(
#         {
#             "id": int(max(testData.productsList, key=lambda x: x["id"])["id"]) + 1,
#             "birthday": birthday,
#             "fio": fio,
#             "phone_number": phoneNumber,
#         }
#     )
#     return RedirectResponse(url="/client", status_code=status.HTTP_303_SEE_OTHER)
