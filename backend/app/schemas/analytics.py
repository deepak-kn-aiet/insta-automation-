"""Pydantic schemas for analytics entities."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AnalyticsBase(BaseModel):
    """Shared analytics fields."""

    automation_id: UUID
    trigger_count: int = Field(default=0, ge=0)


class AnalyticsCreate(AnalyticsBase):
    """Schema for creating analytics data."""


class AnalyticsUpdate(BaseModel):
    """Schema for updating analytics data."""

    automation_id: UUID | None = None
    trigger_count: int | None = Field(default=None, ge=0)


class AnalyticsResponse(AnalyticsBase):
    """Schema returned by the application."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    last_triggered: datetime | None = None
    created_at: datetime
    updated_at: datetime
