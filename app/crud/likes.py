from typing import List

from beanie import PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app import config
from app.models.likes import UserLikes

database_url = config.MONGO_URI
client = AsyncIOMotorClient(database_url)
database_name = config.DATABASE_NAME


async def count_likes(stock_id: PydanticObjectId) -> int:
    likes = await client[database_name][UserLikes.Settings.name].count_documents(
        {"stock_id": stock_id, "liked": True}
    )
    return likes


async def count_dislikes(stock_id: PydanticObjectId) -> int:
    dislikes = await client[database_name][UserLikes.Settings.name].count_documents(
        {"stock_id": stock_id, "liked": False}
    )
    return dislikes
