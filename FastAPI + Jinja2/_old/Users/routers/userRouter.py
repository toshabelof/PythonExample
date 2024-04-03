from typing_extensions import Annotated

from fastapi import APIRouter, Request, Form
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import testData

router = APIRouter(tags=["User"])
templates = Jinja2Templates(directory="Users/templates")


@router.get("/user")
def getAllUsers(req: Request):
    users_list = testData.userList
    return templates.TemplateResponse(
        "usersForm.html", context={"request": req, "users_list": users_list}
    )


@router.get("/user/add")
def addUser(req: Request):
    return templates.TemplateResponse("addUserForm.html", context={"request": req})


@router.post("/user/add")
def addUserPost(
    req: Request,
    login: Annotated[str, Form()],
    password: Annotated[str, Form()],
    fio: Annotated[str, Form()],
    birthday: Annotated[str, Form()],
    phone_number: Annotated[str, Form()],
):
    testData.userList.append(
        {
            "id": int(max(testData.userList, key=lambda x: x["id"])["id"]) + 1,
            "login": login,
            "password": password,
            "fio": fio,
            "birthday": birthday,
            "phone_number": phone_number,
        }
    )
    return RedirectResponse(url="/user", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/user/{id}")
def getUserById(req: Request, id: int):
    user = [d for d in testData.userList if d["id"] == id][0]
    return templates.TemplateResponse(
        "addUserForm.html", context={"request": req, "user": user}
    )
