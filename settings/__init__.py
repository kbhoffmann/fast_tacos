from pydantic_settings import BaseSettings

from .database import database_settings, DatabaseSettings


class Settings(BaseSettings):
    DATABASE: DatabaseSettings = database_settings

settings = Settings()
