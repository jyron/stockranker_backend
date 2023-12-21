from fastapi import HTTPException
from app.models.comment import Comment
from app.models.stock import Stock
from beanie import PydanticObjectId
from app.crud.stocks import get_stock_by_id


async def find_comment_by_id(comment_id: PydanticObjectId) -> Comment:
    comment = await Comment.find_one(Comment.id == comment_id)
    return comment


async def create_comment(
    content: str,
    user_id: str,
    stock_id: PydanticObjectId,
) -> Comment:
    new_comment = Comment(user_id=user_id, content=content, stock_id=stock_id)
    await new_comment.insert()
    return new_comment


async def add_comment_to_stock(comment: Comment, stock: Stock) -> Stock:
    stock.comments.append(comment)
    await stock.save()
    return stock


async def reply_to_comment(reply: Comment, comment: Comment) -> Comment:
    comment.replies.append(reply)
    await comment.save()
    return comment
