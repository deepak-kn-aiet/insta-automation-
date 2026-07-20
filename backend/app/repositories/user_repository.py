"""Repository for managing User model persistence."""

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository handling database operations for the User model."""

    def __init__(self, session: Session) -> None:
        """Initialize UserRepository with the User model and database session.

        Args:
            session (Session): The active SQLAlchemy database session.
        """
        super().__init__(session=session, model=User)
