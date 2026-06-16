from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Knowledge Assistant"
    app_env: str = "development"
    app_version: str = "0.1.0"
    service_name: str = "ai-knowledge-assistant"
    database_url: str | None = None
    openai_api_key: str | None = None
    model_name: str = "gpt-4.1-mini"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
