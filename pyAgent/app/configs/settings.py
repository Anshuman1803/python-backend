from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGO_USER: str
    MONGO_PASS: str
    MONGO_DBNAME: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache(maxsize=1) # Cache the settings to avoid reloading them multiple times
def get_settings() -> Settings:
    return Settings()