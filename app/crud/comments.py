from fastapi import HTTPException
from app.models.comment import Comment
from app.models.stock import Stock
from beanie import PydanticObjectId
from app.crud.stocks import get_stock_by_id

async def find_comment_by_id(comment_id: PydanticObjectId) -> Comment:
    comment = await Comment.find_one({"_id": comment_id})
    return comment

async def create_comment(content: str, user_id: PydanticObjectId, stock_id: PydanticObjectId) -> Comment:
    new_comment = Comment(user_id=user_id, content=content, stock_id=stock_id)
    await new_comment.insert()
    return new_comment

async def create_reply(content: str, user_id: PydanticObjectId, comment_id: PydanticObjectId) -> Comment:
    parent_comment = await find_comment_by_id(comment_id)
    new_reply = Comment(user_id=user_id, content=content, stock_id=parent_comment.stock_id)
    await new_reply.insert()
    parent_comment.replies.append(new_reply)
    await parent_comment.save()
    return new_reply

async def like_comment(comment_id: PydanticObjectId, user_id: PydanticObjectId):
    comment = await find_comment_by_id(comment_id)
    if user_id not in comment.liked_by:  # Assuming liked_by is a list of user_ids who liked the comment
        comment.likes += 1
        comment.liked_by.append(user_id)
        await comment.save()
    return comment

async def get_comments_for_stock(stock_id: PydanticObjectId):
    comments = await Comment.find({"stock_id": stock_id}).to_list()
    return comments
