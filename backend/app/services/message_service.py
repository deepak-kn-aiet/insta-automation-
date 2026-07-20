"""Service for Message domain operations."""

from app.repositories.message_repository import MessageRepository
from app.services.base import BaseService


class MessageService(BaseService[MessageRepository]):
    """Service handling operations for the Message domain."""

    def __init__(self, repository: MessageRepository | None = None) -> None:
        """Initialize MessageService with a MessageRepository.

        Args:
            repository (MessageRepository | None): MessageRepository instance.
        """
        super().__init__(repository=repository)
