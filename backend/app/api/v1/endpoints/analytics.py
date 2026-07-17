"""Placeholder analytics API endpoints."""

from fastapi import APIRouter

from app.api.v1.schemas import MessageResponse

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("", response_model=MessageResponse)
def list_analytics() -> MessageResponse:
    """Placeholder endpoint for analytics."""

    return MessageResponse(message="analytics endpoint coming soon")
