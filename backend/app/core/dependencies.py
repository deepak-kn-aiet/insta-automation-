from fastapi import Depends

from app.config.settings import Settings, settings


class AppDependencies:
    def __init__(self) -> None:
        self.settings = settings

    def get_settings(self) -> Settings:
        return self.settings


app_dependencies = AppDependencies()


def get_settings() -> Settings:
    return app_dependencies.get_settings()
