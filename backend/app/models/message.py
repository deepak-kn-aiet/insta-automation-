"""SQLAlchemy model for conversation messages."""

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


class MessageDirection(str, enum.Enum):
    """Direction of the conversation message."""

    INCOMING = "incoming"
    OUTGOING = "outgoing"


class MessageStatus(str, enum.Enum):
    """Lifecycle status of a message."""

    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"


class Message(TimestampMixin, Base):
    """Stores conversation messages and replies."""

    __tablename__ = "messages"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    instagram_user: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    message: Mapped[str] = mapped_column(String(1000), nullable=False)
    reply: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    direction: Mapped[MessageDirection] = mapped_column(
        Enum(MessageDirection),
        nullable=False,
        default=MessageDirection.INCOMING,
        index=True,
    )
    status: Mapped[MessageStatus] = mapped_column(
        Enum(MessageStatus),
        nullable=False,
        default=MessageStatus.PENDING,
        index=True,
    )

    user: Mapped["User"] = relationship(back_populates="messages")
