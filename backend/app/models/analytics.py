"""SQLAlchemy model for automation analytics."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models._mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.automation import Automation
    from app.models.user import User


class Analytics(TimestampMixin, Base):
    """Stores automation statistics and last-trigger timestamps."""

    __tablename__ = "analytics"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    automation_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("automations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    trigger_count: Mapped[int] = mapped_column(default=0, nullable=False)
    last_triggered: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    user: Mapped["User"] = relationship(back_populates="analytics")
    automation: Mapped["Automation"] = relationship(back_populates="analytics")
