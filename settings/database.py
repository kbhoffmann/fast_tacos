from pydantic_settings import BaseSettings
from typing import ClassVar
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(dotenv_path="./env_files/.env")

class DatabaseSettings(BaseSettings):
        SQLALCHEMY_DATABASE_URL: str = ("postgresql://{}:{}@{}/{}".format(
            os.getenv("PG_USERNAME"),
            os.getenv("PG_PASSWORD"),
            os.getenv("PG_HOST"),
            os.getenv("PG_DATABASE")
        )
    )

database_settings = DatabaseSettings()
