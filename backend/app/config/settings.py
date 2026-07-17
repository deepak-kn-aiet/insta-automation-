"""Shared application settings loaded from environment variables."""

import os
from functools import lru_cache
from typing import Annotated

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    app_name: str = Field(default_factory=lambda: os.getenv('APP_NAME', 'Instagram Automation Assistant'))
    app_version: str = Field(default_factory=lambda: os.getenv('APP_VERSION', '0.1.0'))
    debug: bool = Field(default_factory=lambda: os.getenv('DEBUG', 'false').lower() == 'true')
    database_url: str = Field(default_factory=lambda: os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@localhost:5432/instagram_assistant'))
    redis_url: str = Field(default_factory=lambda: os.getenv('REDIS_URL', ''))
    jwt_secret: str = Field(default_factory=lambda: os.getenv('JWT_SECRET', 'change-me'))
    meta_app_id: str = Field(default_factory=lambda: os.getenv('META_APP_ID', ''))
    meta_app_secret: str = Field(default_factory=lambda: os.getenv('META_APP_SECRET', ''))
    verify_token: str = Field(default_factory=lambda: os.getenv('VERIFY_TOKEN', 'change-me'))
    ollama_url: str = Field(default_factory=lambda: os.getenv('OLLAMA_URL', ''))

    @model_validator(mode='after')
    def validate_required_settings(self) -> 'Settings':
        required_fields = [
            ('DATABASE_URL', self.database_url),
            ('JWT_SECRET', self.jwt_secret),
            ('VERIFY_TOKEN', self.verify_token),
            ('APP_NAME', self.app_name),
            ('APP_VERSION', self.app_version),
        ]
        missing = [name for name, value in required_fields if not value or not str(value).strip()]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        return self


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


def validate_startup_settings() -> Settings:
    settings = get_settings()
    required_fields = [
        ('DATABASE_URL', settings.database_url),
        ('JWT_SECRET', settings.jwt_secret),
        ('VERIFY_TOKEN', settings.verify_token),
        ('APP_NAME', settings.app_name),
        ('APP_VERSION', settings.app_version),
    ]
    missing = [name for name, value in required_fields if not value or not str(value).strip()]
    if missing:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
    return settings


settings = get_settings()
SettingsDependency = Annotated[Settings, Field(default_factory=get_settings)]
