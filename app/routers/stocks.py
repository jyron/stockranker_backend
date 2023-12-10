"""Stocks router endpoints."""

from fastapi import APIRouter
from app.crud.stocks import get_all_stocks, get_stock
from app.models.stock import Stock

stock_router = APIRouter(tags=["stocks"])


@stock_router.get("/stocks")
async def get_stocks():
    stocks = await get_all_stocks()
    return stocks


@stock_router.get("/stocks/{ticker}")
async def get_one_stock(ticker):
    stock = await get_stock(ticker)
    return stock
