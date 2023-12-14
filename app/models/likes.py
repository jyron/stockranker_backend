from beanie import Document
from beanie import init_beanie, PydanticObjectId
from pydantic import BaseModel


class Like(BaseModel):
    user_id: PydanticObjectId
    stock_id: PydanticObjectId
    liked: bool  # True for like, False for dislike


class UserLikes(Document, Like):
    class Settings:
        name = "user_likes"
