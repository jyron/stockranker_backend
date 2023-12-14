"""Stock model."""

from beanie import Document
from typing import Optional


class Stock(Document):
    country: Optional[str]
    currency: Optional[str]
    estimateCurrency: Optional[str]
    exchange: Optional[str]
    finnhubIndustry: Optional[str] = None
    ipo: Optional[str]
    logo: Optional[str] = None
    marketCapitalization: Optional[float]
    name: Optional[str]
    phone: Optional[str] = None
    shareOutstanding: Optional[float]
    ticker: str
    weburl: Optional[str]
    price: Optional[float] = None
    price_change: Optional[float] = None
    percent_change: Optional[float] = None
    high_price_today: Optional[float] = None
    low_price_today: Optional[float] = None
    open_price_today: Optional[float] = None
    previous_close_price: Optional[float] = None
    likes: Optional[int] = None
    dislikes: Optional[int] = None

    class Settings:
        name = "Stock"
