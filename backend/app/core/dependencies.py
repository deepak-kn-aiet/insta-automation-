"""Dependency helpers for shared application settings."""

from typing import Annotated

from fastapi import Depends

from app.core.config import Settings, get_settings


SettingsDependency = Annotated[Settings, Depends(get_settings)]


def get_settings_dependency(settings: SettingsDependency) -> Settings:
    return settings
