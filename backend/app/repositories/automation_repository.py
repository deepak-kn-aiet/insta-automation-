"""Repository for managing Automation model persistence."""

from sqlalchemy.orm import Session

from app.models.automation import Automation
from app.repositories.base import BaseRepository


class AutomationRepository(BaseRepository[Automation]):
    """Repository handling database operations for the Automation model."""

    def __init__(self, session: Session) -> None:
        """Initialize AutomationRepository with the Automation model and database session.

        Args:
            session (Session): The active SQLAlchemy database session.
        """
        super().__init__(session=session, model=Automation)
