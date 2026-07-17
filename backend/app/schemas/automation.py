"""Pydantic schemas for automation entities."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.automation import AutomationReplyType


class AutomationBase(BaseModel):
    """Shared automation fields."""

    keyword: str = Field(..., min_length=1, max_length=100)
    reply_type: AutomationReplyType = AutomationReplyType.TEXT
    reply_text: str | None = Field(default=None, max_length=500)
    media_url: str | None = Field(default=None, max_length=500)
    is_enabled: bool = True


class AutomationCreate(AutomationBase):
    """Schema for creating an automation."""


class AutomationUpdate(BaseModel):
    """Schema for updating an automation."""

    keyword: str | None = Field(default=None, min_length=1, max_length=100)
    reply_type: AutomationReplyType | None = None
    reply_text: str | None = Field(default=None, max_length=500)
    media_url: str | None = Field(default=None, max_length=500)
    is_enabled: bool | None = None


class AutomationResponse(AutomationBase):
    """Schema returned by the application."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
