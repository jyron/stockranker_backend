from typing import Optional, List
from beanie import Document


class Comment(Document):
    user_id: str  # Assuming you have a user ID for identifying the commenter
    content: str
    likes: Optional[int] = 0
    dislikes: Optional[int] = 0
    replies: List["Comment"] = []
