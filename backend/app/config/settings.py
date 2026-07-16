from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "instagram-assistant"
    environment: str = "development"
    debug: bool = True
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"
    database_url: str = "postgresql+psycopg2://postgres:postgres@postgres:5432/instagram_assistant"
    redis_url: str = "redis://redis:6379/0"
    ollama_base_url: str = "http://ollama:11434"
    gemini_api_key: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
