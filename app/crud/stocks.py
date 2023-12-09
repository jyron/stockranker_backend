"""CRUD operations for stocks."""

from app.models.stock import Stock


async def get_stock(ticker):
    stock = await Stock.find_one({"ticker": ticker})
    return stock


async def get_all_stocks():
    stocks = await Stock.find().to_list(length=1000)
    return stocks
