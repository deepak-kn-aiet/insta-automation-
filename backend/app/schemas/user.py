"""Pydantic schemas for user entities."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    """Shared user fields."""

    username: str = Field(..., min_length=3, max_length=50)
    full_name: str | None = Field(default=None, max_length=150)
    is_active: bool = True


class UserCreate(UserBase):
    """Schema for creating a user."""


class UserUpdate(BaseModel):
    """Schema for updating a user."""

    username: str | None = Field(default=None, min_length=3, max_length=50)
    full_name: str | None = Field(default=None, max_length=150)
    is_active: bool | None = None


class UserResponse(UserBase):
    """Schema returned by the application."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime
