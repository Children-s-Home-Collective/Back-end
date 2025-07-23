import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv ()

class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    JWT_SECRET_KEY=os.environ["JWT_SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI= os.environ["DATABASE_URL"]

    DEBUG = os.getenv("DEBUG", "False") == "True"
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    JWT_ACCESS_TOKEN_EXPIRES= timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=8)
    RATELIMIT_HEADERS_ENABLED= True
    