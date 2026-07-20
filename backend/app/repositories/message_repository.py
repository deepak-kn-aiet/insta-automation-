"""Repository for managing Message model persistence."""

from sqlalchemy.orm import Session

from app.models.message import Message
from app.repositories.base import BaseRepository


class MessageRepository(BaseRepository[Message]):
    """Repository handling database operations for the Message model."""

    def __init__(self, session: Session) -> None:
        """Initialize MessageRepository with the Message model and database session.

        Args:
            session (Session): The active SQLAlchemy database session.
        """
        super().__init__(session=session, model=Message)
