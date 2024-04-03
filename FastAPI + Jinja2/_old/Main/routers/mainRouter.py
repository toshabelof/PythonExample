from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

import testData

router = APIRouter(
    tags=['Login']
)
templates = Jinja2Templates(directory="Main/templates")


@router.get('/')
def getMain(req: Request):
    if len(testData.userData) == 0:
        return RedirectResponse(url='/login', status_code=status.HTTP_303_SEE_OTHER)
    else:
        return templates.TemplateResponse('mainForm.html', context={'request': req, 'user': testData.userData})


@router.get('/logout')
def logout(req: Request):
    testData.userData = {}
    return RedirectResponse(url='/login', status_code=status.HTTP_303_SEE_OTHER)