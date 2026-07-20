"""Service for User domain operations."""

from typing import Any
from uuid import UUID

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.base import BaseService


class UserService(BaseService[UserRepository]):
    """Service handling operations for the User domain."""

    def __init__(self, repository: UserRepository | None = None) -> None:
        """Initialize UserService with a UserRepository.

        Args:
            repository (UserRepository | None): UserRepository instance.
        """
        super().__init__(repository=repository)

    def _get_repository(self) -> UserRepository:
        """Ensure repository is initialized and return instance."""
        if self.repository is None:
            raise RuntimeError("UserRepository is not initialized.")
        return self.repository

    def create_user(self, user_data: dict[str, Any] | User) -> User:
        """Create a new user.

        Args:
            user_data (dict[str, Any] | User): Validated user attributes or User model instance.

        Returns:
            User: Created user instance.
        """
        return self._get_repository().create(user_data)

    def get_user_by_id(self, user_id: UUID | Any) -> User | None:
        """Retrieve a user by primary key ID.

        Args:
            user_id (UUID | Any): Primary key identifier of the user.

        Returns:
            User | None: User instance if found, otherwise None.
        """
        return self._get_repository().get_by_id(user_id)

    def get_all_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """Retrieve all users with pagination.

        Args:
            skip (int): Number of user records to skip. Defaults to 0.
            limit (int): Maximum number of user records to return. Defaults to 100.

        Returns:
            list[User]: List of retrieved users.
        """
        return self._get_repository().get_all(skip=skip, limit=limit)

    def delete_user(self, user_id: UUID | Any) -> bool:
        """Delete a user by primary key ID.

        Args:
            user_id (UUID | Any): Primary key identifier of the user to delete.

        Returns:
            bool: True if user was deleted, False if user was not found.
        """
        return self._get_repository().delete(user_id)
