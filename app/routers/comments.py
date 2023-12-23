from app.models.comment import Comment
from app.crud.comments import (
    add_reply_to_comment,
    create_comment,
    find_comment_by_id,
    add_comment_to_stock,
    create_reply,
)
from fastapi import APIRouter, HTTPException, Depends, Body
from beanie import PydanticObjectId
from app.auth.usermanager import current_active_user
from app.models.users import User
from app.models.stock import Stock
from app.models.comment import Comment


comment_router = APIRouter(tags=["comments"])


@comment_router.post("/stock_comment")
async def add_comment(
    comment_data=Body(...),
    user=Depends(current_active_user),
):
    content = comment_data["comment"]
    stock_id = comment_data["stock_id"]
    user_id = user.id
    try:
        comment = await create_comment(
            user_id=user_id, stock_id=stock_id, content=content
        )
        stock = await Stock.find_one(Stock.id == comment.stock_id)
        new = await add_comment_to_stock(comment, stock)
        print(new.comments)
        return new.comments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@comment_router.post("/reply_comment")
async def get_reply_comment(
    reply_data=Body(...),
    user=Depends(current_active_user),
):
    content = reply_data["content"]
    comment_id = reply_data["comment_id"]
    stock_id = reply_data["stock_id"]
    user_id = user.id
    try:
        reply = Comment(stock_id=stock_id, user_id=user_id, content=content)
        await reply.insert()
        comment = await find_comment_by_id(comment_id)
        replied_comment = await add_reply_to_comment(reply, comment)
        return replied_comment
    except Exception as e:
        print(e)
