from typing_extensions import Annotated

from fastapi import APIRouter, Request, Form
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from models.user import UserModel

router = APIRouter(tags=["Client"])
templates = Jinja2Templates(directory="templates")


@router.get("/users")
def get_users(req: Request):
    users = UserModel.get_users()
    return templates.TemplateResponse(
        "UsersForm.html", context={"request": req, "users_list": users}
    )


@router.get("/users/ro/{isn}")
def get_users_read_only(req: Request, isn: int):
    user = UserModel.get_user_by_id(isn)
    return templates.TemplateResponse(
        "UserForm.html", context={"request": req, "user": user, "readonly": True}
    )


@router.get("/users/{isn}")
def get_users(req: Request, isn: int):
    user = UserModel.get_user_by_id(isn)
    return templates.TemplateResponse(
        "UserForm.html", context={"request": req, "user": user, "readonly": False}
    )


@router.post("/users/{isn}")
def get_users(req: Request, isn: int, fio: Annotated[str, Form()]):
    user = UserModel.get_user_by_id(isn)
    user.upd(fio)
    return RedirectResponse(
        url=f"/users/ro/{isn}", status_code=status.HTTP_303_SEE_OTHER
    )


@router.post("/users/delete/{isn}")
def get_users(req: Request, isn: int):
    UserModel.delete_user_by_id(isn)
    return RedirectResponse(url="/users", status_code=status.HTTP_303_SEE_OTHER)


# @router.get("/client/add")
# def addClient(req: Request):
#     return templates.TemplateResponse("addClientForm.html", context={"request": req})
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
