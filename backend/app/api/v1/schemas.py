"""Reusable response schemas for the API foundation."""

from __future__ import annotations

from pydantic import BaseModel, Field


class SuccessResponse(BaseModel):
    """Generic success payload."""

    success: bool = True
    message: str = Field(default="request completed successfully")


class ErrorResponse(BaseModel):
    """Generic error payload."""

    success: bool = False
    error: str
    detail: str | None = None


class MessageResponse(BaseModel):
    """Simple message payload for placeholder endpoints."""

    message: str


class HealthResponse(BaseModel):
    """Health-check response for the versioned API."""

    status: str
    database: str
    version: str
    timestamp: str
