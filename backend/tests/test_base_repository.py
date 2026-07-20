"""Tests for generic BaseRepository CRUD operations."""

from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.base import Base
from app.models.user import User
from app.repositories.base import BaseRepository
from app.repositories.user_repository import UserRepository


@pytest.fixture
def db_session() -> Session:
    """Fixture that provides an in-memory SQLite database session."""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = testing_session_local()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def user_repo(db_session: Session) -> UserRepository:
    """Fixture providing a UserRepository instance."""
    return UserRepository(db_session)


def test_create(user_repo: UserRepository) -> None:
    """Verify object creation, primary key generation, and returned instance."""
    user = user_repo.create({"username": "johndoe", "full_name": "John Doe"})

    assert user is not None
    assert user.id is not None
    assert user.username == "johndoe"
    assert user.full_name == "John Doe"
    assert user.is_active is True


def test_get_by_id(user_repo: UserRepository) -> None:
    """Verify fetching existing object by ID and None for non-existing ID."""
    created_user = user_repo.create({"username": "janedoe", "full_name": "Jane Doe"})

    fetched_user = user_repo.get_by_id(created_user.id)
    assert fetched_user is not None
    assert fetched_user.id == created_user.id
    assert fetched_user.username == "janedoe"

    non_existent = user_repo.get_by_id(uuid4())
    assert non_existent is None


def test_get_all(user_repo: UserRepository) -> None:
    """Verify get_all returns a list of all inserted records."""
    users_before = user_repo.get_all()
    assert isinstance(users_before, list)
    assert len(users_before) == 0

    user1 = user_repo.create({"username": "user1", "full_name": "User One"})
    user2 = user_repo.create({"username": "user2", "full_name": "User Two"})

    users_after = user_repo.get_all()
    assert isinstance(users_after, list)
    assert len(users_after) == 2
    user_ids = {u.id for u in users_after}
    assert user1.id in user_ids
    assert user2.id in user_ids


def test_update(user_repo: UserRepository) -> None:
    """Verify object fields are updated and updated instance is returned."""
    user = user_repo.create({"username": "alice", "full_name": "Alice Smith"})

    updated_user = user_repo.update(user, {"full_name": "Alice Johnson", "is_active": False})

    assert updated_user is not None
    assert updated_user.id == user.id
    assert updated_user.full_name == "Alice Johnson"
    assert updated_user.is_active is False

    refetched_user = user_repo.get_by_id(user.id)
    assert refetched_user is not None
    assert refetched_user.full_name == "Alice Johnson"


def test_delete(user_repo: UserRepository) -> None:
    """Verify object removal and non-existence after deletion."""
    user = user_repo.create({"username": "bob", "full_name": "Bob Brown"})
    user_id = user.id

    assert user_repo.get_by_id(user_id) is not None

    deleted = user_repo.delete(user_id)
    assert deleted is True

    assert user_repo.get_by_id(user_id) is None

    assert user_repo.delete(uuid4()) is False


def test_base_repository_generic_standalone(db_session: Session) -> None:
    """Verify BaseRepository works directly with generic model typing."""
    generic_repo = BaseRepository(db_session, User)
    user = generic_repo.create({"username": "standalone_user"})

    assert user.id is not None
    assert generic_repo.get_by_id(user.id) is not None
    assert generic_repo.delete(user.id) is True
