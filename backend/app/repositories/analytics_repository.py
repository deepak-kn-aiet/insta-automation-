"""Repository for managing Analytics model persistence."""

from sqlalchemy.orm import Session

from app.models.analytics import Analytics
from app.repositories.base import BaseRepository


class AnalyticsRepository(BaseRepository[Analytics]):
    """Repository handling database operations for the Analytics model."""

    def __init__(self, session: Session) -> None:
        """Initialize AnalyticsRepository with the Analytics model and database session.

        Args:
            session (Session): The active SQLAlchemy database session.
        """
        super().__init__(session=session, model=Analytics)
