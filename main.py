import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.database import init_database
from app.routers.stocks import stock_router
from app.routers.users import user_router
from app.scheduler import setup_scheduler
from app.update_service import update_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    await setup_scheduler()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/api/v0")
app.include_router(stock_router, prefix="/api/v0")
app.include_router(update_router, prefix="/api/v0")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        log_level="info",
        reload=True,
    )
