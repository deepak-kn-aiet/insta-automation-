"""SQLAlchemy model for automation rules."""

from __future__ import annotations

import enum
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models._mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.user import User


class AutomationReplyType(str, enum.Enum):
    """Supported automation reply strategies."""

    TEXT = "text"
    MEDIA = "media"
    MIXED = "mixed"


class Automation(TimestampMixin, Base):
    """Stores automation rules for matching keywords and replies."""

    __tablename__ = "automations"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    keyword: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    reply_type: Mapped[AutomationReplyType] = mapped_column(
        Enum(AutomationReplyType),
        nullable=False,
        default=AutomationReplyType.TEXT,
        index=True,
    )
    reply_text: Mapped[str | None] = mapped_column(String(500), nullable=True)
    media_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    is_enabled: Mapped[bool] = mapped_column(default=True, nullable=False)

    user: Mapped["User"] = relationship(back_populates="automations")
