from datetime import datetime

from typing_extensions import Annotated

from fastapi import APIRouter,Request, Form
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from Users.models.userModel import UserModel
import testData

router = APIRouter(
    tags=['Login']
)
templates = Jinja2Templates(directory="Users/templates")


@router.get('/registration')
def login(req: Request):
    return templates.TemplateResponse('registrationForm.html', context={'request': req})


@router.post('/registration')
def login(req: Request,
          login: Annotated[str, Form()],
          password: Annotated[str, Form()],
          name: Annotated[str, Form()],
          birthday: Annotated[str, Form()],
          phone_number: Annotated[str, Form()]):
    user = UserModel(login=login,
                     password=password,
                     fio=name,
                     birthday=birthday,
                     phone_number=phone_number)
    user.add()
    testData.userData = [d for d in testData.userList if d['login'] == login][0]
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)