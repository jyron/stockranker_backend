"""Scheduler updates stock prices every 30 minutes"""

from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.update_service import get_sp500_tickers, update_stock_prices


async def setup_scheduler():
    scheduler = AsyncIOScheduler()
    initial_run_time = datetime.now() + timedelta(seconds=5)
    tickers = await get_sp500_tickers()
    scheduler.add_job(
        update_stock_prices,
        "interval",
        minutes=30,
        args=[tickers],
        next_run_time=initial_run_time,
    )
    scheduler.start()
