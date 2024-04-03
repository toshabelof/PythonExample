from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

import testData

router = APIRouter(tags=["Products"])
templates = Jinja2Templates(directory="templates")


@router.get("/products")
def get_all_products(req: Request):
    products = testData.productsList
    return templates.TemplateResponse(
        "ProductsForm.html", context={"request": req, "product_list": products}
    )


# @router.get("/product/add")
# def addProducts(req: Request):
#     return templates.TemplateResponse("addProductsForm.html", context={"request": req})
#
#
# @router.post("/product/add")
# def saveProducts(
#     req: Request,
#     name: Annotated[str, Form()],
#     unit: Annotated[str, Form()],
#     weight: Annotated[str, Form()],
#     width: Annotated[str, Form()],
#     height: Annotated[str, Form()],
#     length: Annotated[str, Form()],
#     cost_price: Annotated[str, Form()],
#     selling_price: Annotated[str, Form()],
# ):
#     testData.productsList.append(
#         {
#             "id": int(max(testData.productsList, key=lambda x: x["id"])["id"]) + 1,
#             "name": name,
#             "unit": unit,
#             "weight": weight,
#             "width": width,
#             "height": height,
#             "length": length,
#             "cost_price": cost_price,
#             "selling_price": selling_price,
#         }
#     )
#     return RedirectResponse(url="/product", status_code=status.HTTP_303_SEE_OTHER)
#
#
# @router.get("/product/{id}")
# def addProducts(req: Request, id: int):
#     product = [d for d in testData.productsList if d["id"] == id][0]
#     return templates.TemplateResponse(
#         "viewProductForm.html", context={"request": req, "product": product}
#     )
