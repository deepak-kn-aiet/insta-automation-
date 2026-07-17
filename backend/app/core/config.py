"""Compatibility wrapper for the shared application settings."""

from app.config.settings import Settings, SettingsDependency, get_settings, settings

__all__ = ["Settings", "SettingsDependency", "get_settings", "settings"]
