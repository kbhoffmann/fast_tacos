from settings import BaseSettings
from typing import Any
from .base import env

class DatabaseSettings(BaseSettings):
        SQLALCHEMY_DATABASE_URL: str = ("postgresql://{}:{}@{}:{}/{}".format(
            env.str("PG_USERNAME"),
            env.str("PG_PASSWORD"),
            env.str("PG_HOST"),
            env.str("PG_PORT", 5432),
            env.str("PG_DATABASE")
        )
    )

database_settings = DatabaseSettings()
