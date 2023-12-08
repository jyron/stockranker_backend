import os

from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
SECRET = os.getenv("SECRET")
DATABASE_NAME = os.getenv("DATABASE_NAME")
