# get aall stocks from database

from app.models.stock import Stock


async def get_all_stocks():
    stocks = await Stock.find().to_list(length=1000)
    return stocks
