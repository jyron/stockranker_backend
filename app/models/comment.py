from typing import Optional, List
from beanie import Document, PydanticObjectId
from datetime import datetime, timezone


class Comment(Document):
    user_id: PydanticObjectId
    stock_id: PydanticObjectId
    content: str
    likes: Optional[int] = 0
    dislikes: Optional[int] = 0
    replies: List["Comment"] = []
    created_at: Optional[datetime] = datetime.now(timezone.utc)

    def increment_likes(self):
        self.likes += 1
        return self.save()

