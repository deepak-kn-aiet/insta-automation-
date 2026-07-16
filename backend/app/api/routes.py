from fastapi import APIRouter, Depends

from app.core.dependencies import get_settings
from app.schemas.health import HealthResponse
from app.services.automation_service import AutomationService

router = APIRouter()


@router.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {"message": "Instagram Automation Assistant API"}


@router.get("/health", tags=["health"], response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", app="instagram-assistant")


@router.get("/automation/status", tags=["automation"])
def automation_status() -> dict[str, object]:
    service = AutomationService()
    return service.get_status()
