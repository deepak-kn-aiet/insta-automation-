"""Health-related API endpoints."""

from datetime import datetime, timezone

from fastapi import APIRouter

from app.api.v1.schemas import HealthResponse
from app.core.config import get_settings

router = APIRouter(tags=["health"])
settings = get_settings()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return a simple health payload for the API."""

    database_status = "connected"
    try:
        from sqlalchemy import text
        from app.database.database import engine

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception:
        database_status = "unavailable"

    return HealthResponse(
        status="ok",
        database=database_status,
        version=settings.app_version,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
