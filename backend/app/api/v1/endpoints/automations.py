"""Placeholder automation API endpoints."""

from fastapi import APIRouter

from app.api.v1.schemas import MessageResponse

router = APIRouter(prefix="/automations", tags=["automations"])


@router.get("", response_model=MessageResponse)
def list_automations() -> MessageResponse:
    """Placeholder endpoint for automations."""

    return MessageResponse(message="automations endpoint coming soon")
