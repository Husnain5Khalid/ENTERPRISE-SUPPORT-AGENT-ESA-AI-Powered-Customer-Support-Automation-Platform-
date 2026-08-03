from functools import lru_cache # lru_cahce =Least Recently Used. lru_cache is a decorator that caches(temporary storage) the result of a function.


from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Enterprise Support Agent"

    google_api_key: str = Field(..., alias="GOOGLE_API_KEY")

    model_name: str = Field(..., alias="MODEL_NAME")

    database_url: str = Field(..., alias="DATABASE_URL")

    chroma_db_path: str = Field(..., alias="CHROMA_DB_PATH")

    log_level: str = Field("INFO", alias="LOG_LEVEL")


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()


settings = get_settings()

