from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "LIFE-OS"
    app_version: str = "0.1.0"

    host: str = "127.0.0.1"
    port: int = 8000

    llm_provider: str = "ollama"
    llm_model: str = "dolphin3:latest"
    ollama_host: str = "http://localhost:11434"

    database_url: str = "sqlite:///lifeos.db"

    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()