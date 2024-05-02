from pydantic import BaseSettings

# from .base import env
from .database import database_settings, DatabaseSettings


class Settings(BaseSettings):
    # LOG_LEVEL: str = env.str("LOG_LEVEL", "INFO")
    DATABASE: DatabaseSettings = database_settings
    # LOG_SETTINGS: dict = logging_settings.config
    # ENV: str = env.str("ENV")

settings = Settings()
