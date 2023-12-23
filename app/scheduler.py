"""Scheduler updates stock prices every 30 minutes"""

from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.update_service import (
    get_sp500_tickers,
    update_stock_prices,
    create_stock_profiles,
)


async def setup_scheduler():
    scheduler = AsyncIOScheduler()
    initial_run_time = datetime.now() + timedelta(seconds=5)
    tickers = await get_sp500_tickers()
    scheduler.add_job(
        create_stock_profiles,
        "date",
        run_date=initial_run_time,
        args=[tickers],
    )
    # scheduler.add_job(
    #     update_stock_prices,
    #     "interval",
    #     minutes=30,
    #     args=[tickers],
    #     next_run_time=initial_run_time,
    #     depends_on="create_stock_profiles",
    # )
    scheduler.start()
