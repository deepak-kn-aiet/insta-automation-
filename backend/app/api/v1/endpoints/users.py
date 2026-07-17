"""Placeholder users API endpoints."""

from fastapi import APIRouter

from app.api.v1.schemas import MessageResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=MessageResponse)
def list_users() -> MessageResponse:
    """Placeholder endpoint for users."""

    return MessageResponse(message="users endpoint coming soon")
