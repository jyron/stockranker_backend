from fastapi import APIRouter, HTTPException, Depends
from beanie import PydanticObjectId
from app.auth.usermanager import current_active_user
from app.models.comment import Comment
from app.crud.comments import (
    create_comment,
    create_reply,
    like_comment,
    get_comments_for_stock
)
from pydantic import BaseModel

class CommentData(BaseModel):
    comment: str

class ReplyData(BaseModel):
    content: str
    comment_id: PydanticObjectId

comment_router = APIRouter(tags=["comments"])

@comment_router.post("/stock/{stock_id}/comment")
async def add_comment_to_stock(stock_id: PydanticObjectId, comment_data: CommentData, user= Depends(current_active_user)):
    try:
        comment = await create_comment(content=comment_data.comment, user_id=user.id, stock_id=stock_id)
        return {"message": "Comment added successfully", "comment": comment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@comment_router.get("/stock/{stock_id}/comments")
async def get_comments_for_stock(stock_id: PydanticObjectId):
    try:
        comments = await get_comments_for_stock(stock_id)
        return comments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@comment_router.post("/reply_comment")
async def reply_comment(reply_data: ReplyData, user= Depends(current_active_user)):
    try:
        reply = await create_reply(content=reply_data.content, user_id=user.id, comment_id=reply_data.comment_id)
        return {"message": "Reply added successfully", "reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@comment_router.post("/like_comment/{comment_id}")
async def like_a_comment(comment_id: PydanticObjectId, user= Depends(current_active_user)):
    try:
        comment = await like_comment(comment_id=comment_id, user_id=user.id)
        return {"message": "Comment liked successfully", "likes": comment.likes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

