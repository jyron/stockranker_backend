import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_database
from app.routers.stocks import stock_router
from app.routers.users import user_router
from app.scheduler import setup_scheduler
from app.update_service import update_router
from app.routers.comments import comment_router
from app.routers.alphavantage import avrouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    # await setup_scheduler()
    yield


app = FastAPI(lifespan=lifespan)
origins = [
    "https://stockranker.co",
    "http://stockranker.co",
    "https://www.stockranker.co",
    "http://www.stockranker.co",
    "localhost:5173",
    "https://main--whimsical-monstera-b5072e.netlify.app",
    "http://localhost:5173",
]
origins = origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
app.include_router(user_router, prefix="/api/v0")
app.include_router(stock_router, prefix="/api/v0")
app.include_router(update_router, prefix="/api/v0")
app.include_router(comment_router, prefix="/api/v0")
app.include_router(avrouter, prefix="/api/v0")

# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         log_level="info",
#         reload=True,
#     )
