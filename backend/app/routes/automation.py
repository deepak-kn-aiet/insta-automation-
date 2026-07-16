from fastapi import APIRouter

from app.services.automation_service import AutomationService

router = APIRouter(prefix="/automation", tags=["automation"])


@router.get("/status")
def automation_status() -> dict[str, object]:
    service = AutomationService()
    return service.get_status()
