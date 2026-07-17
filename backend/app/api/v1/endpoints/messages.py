"""Placeholder messages API endpoints."""

from fastapi import APIRouter

from app.api.v1.schemas import MessageResponse

router = APIRouter(prefix="/messages", tags=["messages"])


@router.get("", response_model=MessageResponse)
def list_messages() -> MessageResponse:
    """Placeholder endpoint for messages."""

    return MessageResponse(message="messages endpoint coming soon")
