from fastapi import APIRouter
from app.crud.stocks import get_all_stocks
from app.models.stock import Stock

stock_router = APIRouter()


@stock_router.get("/stocks")
async def get_stocks():
    stocks = await get_all_stocks()
    return stocks
