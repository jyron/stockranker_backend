"""Update service for stock data."""

import asyncio
import time

import finnhub
from datapackage import Package
from fastapi import APIRouter

from app import config
from app.models.stock import Stock

finnhub_client = finnhub.Client(api_key=config.FINNHUB_API_KEY)
update_router = APIRouter(tags=["update"])


async def get_sp500_tickers():
    package = Package("https://datahub.io/core/s-and-p-500-companies/datapackage.json")
    stocks = package.get_resource("constituents").read(keyed=True)
    tickers = [stock["Symbol"] for stock in stocks]
    return tickers


async def create_stock_profile(ticker):
    existing_stock = await Stock.find_one({"ticker": ticker})
    if existing_stock:
        print(f"{existing_stock.ticker} stock already exists")
        return
    stock_data = finnhub_client.company_profile2(symbol=ticker)

    stock_profile = Stock(**stock_data)
    await stock_profile.insert()
    time.sleep(1)
    print(f"{stock_profile.ticker} stock added to DB")


async def create_stock_profiles(tickers):
    for ticker in tickers:
        try:
            await create_stock_profile(ticker)
        except Exception as e:
            print(e, ticker)


async def update_stock_price(ticker):
    price = finnhub_client.quote(ticker)
    stock = await Stock.find_one({"ticker": ticker})
    stock.price = price["c"]
    stock.price_change = price["d"]
    stock.percent_change = price["dp"]
    stock.high_price_today = price["h"]
    stock.low_price_today = price["l"]
    stock.open_price_today = price["o"]
    stock.previous_close_price = price["pc"]
    print(f"{stock.name} price updated: {stock.price}")
    await stock.save()


async def update_stock_prices(tickers):
    for ticker in tickers:
        try:
            await update_stock_price(ticker)
            time.sleep(1.001)
        except Exception as e:
            print(e, ticker)
