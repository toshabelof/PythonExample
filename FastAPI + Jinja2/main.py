import uvicorn
from fastapi import FastAPI

from routers import ClientRouter, ProductRouter, StatisticsRouter, UserRouter

app = FastAPI()
app.include_router(UserRouter.router)
app.include_router(ClientRouter.router)
app.include_router(ProductRouter.router)
app.include_router(StatisticsRouter.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
