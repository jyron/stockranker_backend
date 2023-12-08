from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.database import init_database
from app.routers.users import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/api/v0")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
