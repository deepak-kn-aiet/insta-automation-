"""Unit tests for UserService using mocked UserRepository."""

from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


@pytest.fixture
def mock_user_repo() -> MagicMock:
    """Fixture providing a mock UserRepository."""
    return MagicMock(spec=UserRepository)


@pytest.fixture
def user_service(mock_user_repo: MagicMock) -> UserService:
    """Fixture providing a UserService instance with injected mock repository."""
    return UserService(repository=mock_user_repo)


def test_create_user(user_service: UserService, mock_user_repo: MagicMock) -> None:
    """Verify create_user delegates to UserRepository.create and returns created user."""
    mock_user = User(id=uuid4(), username="testuser", full_name="Test User")
    mock_user_repo.create.return_value = mock_user

    user_data = {"username": "testuser", "full_name": "Test User"}
    result = user_service.create_user(user_data)

    mock_user_repo.create.assert_called_once_with(user_data)
    assert result == mock_user
    assert result.username == "testuser"


def test_get_user_by_id(user_service: UserService, mock_user_repo: MagicMock) -> None:
    """Verify get_user_by_id returns user if found and None if missing."""
    user_id = uuid4()
    mock_user = User(id=user_id, username="existing_user")
    mock_user_repo.get_by_id.side_effect = lambda uid: mock_user if uid == user_id else None

    # Found case
    found_user = user_service.get_user_by_id(user_id)
    mock_user_repo.get_by_id.assert_called_with(user_id)
    assert found_user == mock_user

    # Missing case
    missing_id = uuid4()
    missing_user = user_service.get_user_by_id(missing_id)
    mock_user_repo.get_by_id.assert_called_with(missing_id)
    assert missing_user is None


def test_get_all_users(user_service: UserService, mock_user_repo: MagicMock) -> None:
    """Verify get_all_users delegates pagination and returns list of users."""
    mock_users = [
        User(id=uuid4(), username="user1"),
        User(id=uuid4(), username="user2"),
    ]
    mock_user_repo.get_all.return_value = mock_users

    users = user_service.get_all_users(skip=0, limit=50)

    mock_user_repo.get_all.assert_called_once_with(skip=0, limit=50)
    assert users == mock_users
    assert len(users) == 2


def test_delete_user(user_service: UserService, mock_user_repo: MagicMock) -> None:
    """Verify delete_user delegates to UserRepository.delete and returns boolean result."""
    user_id = uuid4()
    mock_user_repo.delete.side_effect = lambda uid: uid == user_id

    # Success case
    assert user_service.delete_user(user_id) is True
    mock_user_repo.delete.assert_called_with(user_id)

    # Missing case
    missing_id = uuid4()
    assert user_service.delete_user(missing_id) is False
    mock_user_repo.delete.assert_called_with(missing_id)
