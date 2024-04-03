from fastapi import APIRouter, Request, Form
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from typing_extensions import Annotated

import testData

router = APIRouter(
    tags=['Login']
)
templates = Jinja2Templates(directory="Users/templates")


@router.get('/login')
def login(req: Request):
    return templates.TemplateResponse('loginForm.html', context={'request': req})


@router.post('/login')
def login(req: Request, login: Annotated[str, Form()], password: Annotated[str, Form()]):
    try:
        testData.userData = [d for d in testData.userList if d['login'] == login and d['password'] == password][0]
        return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)
    except:
        return status.HTTP_404_NOT_FOUND
