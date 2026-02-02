from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    # App settings
    app_name: str = "Todo Backend API"
    app_version: str = "1.0.0"
    debug: bool = True

    # Database (REQUIRED)
    database_url: str

    # JWT
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30

    # Frontend
    frontend_url: str = "https://muhammad-rehan.github.io/Full-Stack-Todo-Web-Application"

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_password: Optional[str] = None

    # Logging
    log_level: str = "INFO"

    # OpenAI/OpenRouter
    openai_api_key: str
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_model: str = "google/gemini-2.0-flash-exp:free"
    use_openrouter: bool = False  # Flag to switch between OpenAI and OpenRouter

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
