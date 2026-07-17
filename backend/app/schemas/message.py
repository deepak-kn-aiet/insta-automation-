"""Pydantic schemas for message entities."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.message import MessageDirection, MessageStatus


class MessageBase(BaseModel):
    """Shared message fields."""

    instagram_user: str = Field(..., min_length=1, max_length=100)
    message: str = Field(..., min_length=1, max_length=1000)
    reply: str | None = Field(default=None, max_length=1000)
    direction: MessageDirection = MessageDirection.INCOMING
    status: MessageStatus = MessageStatus.PENDING


class MessageCreate(MessageBase):
    """Schema for creating a message."""


class MessageUpdate(BaseModel):
    """Schema for updating a message."""

    instagram_user: str | None = Field(default=None, min_length=1, max_length=100)
    message: str | None = Field(default=None, min_length=1, max_length=1000)
    reply: str | None = Field(default=None, max_length=1000)
    direction: MessageDirection | None = None
    status: MessageStatus | None = None


class MessageResponse(MessageBase):
    """Schema returned by the application."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
