"""CRUD operations for stocks."""

from beanie import PydanticObjectId

from app.crud.likes import count_dislikes, count_likes
from app.models.likes import UserLikes
from app.models.stock import Stock


async def get_stock(ticker):
    ticker = ticker.upper()
    stock = await Stock.find_one({"ticker": ticker})
    return stock


async def get_all_stocks():
    stocks = await Stock.find().to_list(length=1000)
    return stocks


async def like_stock(
    user_id: PydanticObjectId, stock_id: PydanticObjectId, liked: bool
):
    # Check if the user has already liked or disliked the stock
    like = await UserLikes.find_one({"user_id": user_id, "stock_id": stock_id})
    if like:
        # If the user has already liked or disliked the stock, update the like
        like.liked = liked
        await like.save()
    else:
        # If the user has not already liked or disliked the stock, create a new like
        like = UserLikes(user_id=user_id, stock_id=stock_id, liked=liked)
        await like.insert()
    print("Liked Stock:", like)


async def update_stock_likes(stock_id: PydanticObjectId):
    stock = await Stock.find_one(Stock.id == stock_id)
    likes = await count_likes(stock_id)
    dislikes = await count_dislikes(stock_id)

    # Update the stock's likes and dislikes
    stock.likes = likes
    stock.dislikes = dislikes
    await stock.save()
    print("Update Stock Likes:", stock.ticker, stock.likes, stock.dislikes)
