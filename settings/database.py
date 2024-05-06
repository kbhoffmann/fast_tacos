from settings import BaseSettings
from typing import Any
from .base import env

class DatabaseSettings(BaseSettings):
        SQLALCHEMY_DATABASE_URL: str = ("postgresql://{}:{}@{}:{}/{}".format(
            env.str("POSTGRES_USER"),
            env.str("POSTGRES_PASSWORD"),
            env.str("PG_HOST"),
            env.str("PG_PORT", 5432),
            env.str("POSTGRES_DB")
        )
    )

database_settings = DatabaseSettings()
