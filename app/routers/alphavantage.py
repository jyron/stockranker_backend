import requests
from app import config
from fastapi import APIRouter
import json
from pprint import pprint

ALPHAVANTAGE_API_KEY = config.ALPHAVANTAGE_API_KEY

avrouter = APIRouter(tags=["alphavantage"])


@avrouter.get("/gainers_losers")
async def get_gainers_losers():
    url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={ALPHAVANTAGE_API_KEY}"
    r = requests.get(url)
    data = r.json()
    return data


@avrouter.get("/news")
async def get_news():
    data = "app/news_data.json"

    with open(data, "r") as json_file:
        news_data = json.load(json_file)
    stories = news_data["feed"]
    # pprint(stories[:10])
    return stories[:10]
