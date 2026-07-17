from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(tags=["root"])
settings = get_settings()


@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "app": "instagram-assistant",
        "version": settings.app_version,
        "status": "running",
    }
