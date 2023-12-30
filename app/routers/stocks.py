"""Stocks router endpoints."""

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends

from app.auth.usermanager import current_active_user
from app.crud.likes import count_dislikes, count_likes
from app.crud.stocks import get_all_stocks, get_stock, like_stock, update_stock_likes
from app.models.stock import Stock

stock_router = APIRouter(tags=["stocks"])


@stock_router.get("/stocks")
async def get_stocks_in_order_of_likes():
    stocks = await Stock.find().sort(-Stock.marketCapitalization).to_list(length=1000)
    return stocks


@stock_router.get("/stocks/{ticker}")
async def get_one_stock(ticker):
    stock = await get_stock(ticker)
    return stock


@stock_router.post("/stocks/{stock_id}/like")
async def like_one_stock(stock_id: PydanticObjectId, user=Depends(current_active_user)):
    await like_stock(user_id=user.id, stock_id=stock_id, liked=True)
    await update_stock_likes(stock_id)


@stock_router.post("/stocks/{stock_id}/dislike")
async def dislike_one_stock(
    stock_id: PydanticObjectId, user=Depends(current_active_user)
):
    await like_stock(user_id=user.id, stock_id=stock_id, liked=False)
    await update_stock_likes(stock_id)


@stock_router.get("/stocks/comments/{stock_id}")
async def get_stock_comments(stock_id: PydanticObjectId):
    stock = await Stock.find_one(Stock.id == stock_id)
    return stock.comments
