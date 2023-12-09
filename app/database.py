from beanie import init_beanie, Document
from fastapi_users_db_beanie import BeanieUserDatabase
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from app.models.users import User
from app.models.stock import Stock
from app import config


async def init_database():
    client = AsyncIOMotorClient(config.MONGO_URI)
    document_models = [User, Stock]
    await init_beanie(
        database=client[config.DATABASE_NAME], document_models=document_models
    )


async def get_user_db():
    yield BeanieUserDatabase(User)
