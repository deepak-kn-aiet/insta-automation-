"""Generic base repository for SQLAlchemy models."""

from typing import Any, Generic, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """Generic base repository providing common database context and access for model repositories.

    Attributes:
        session (Session): The SQLAlchemy database session.
        model (Type[ModelType]): The SQLAlchemy model class associated with the repository.
    """

    def __init__(self, session: Session, model: Type[ModelType]) -> None:
        """Initialize the BaseRepository.

        Args:
            session (Session): The active SQLAlchemy database session.
            model (Type[ModelType]): The SQLAlchemy model class.
        """
        self.session = session
        self.model = model

    def create(self, attributes: dict[str, Any] | ModelType) -> ModelType:
        """Create and persist a new model instance.

        Args:
            attributes (dict[str, Any] | ModelType): Attribute dictionary or model instance.

        Returns:
            ModelType: The created and refreshed model instance.

        Raises:
            RuntimeError: If a database operation fails.
        """
        try:
            if isinstance(attributes, dict):
                instance = self.model(**attributes)
            else:
                instance = attributes
            self.session.add(instance)
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except SQLAlchemyError as exc:
            self.session.rollback()
            raise RuntimeError(f"Failed to create {self.model.__name__}: {exc}") from exc

    def get_by_id(self, id: Any) -> ModelType | None:
        """Fetch a single record by its primary key ID.

        Args:
            id (Any): Primary key identifier.

        Returns:
            ModelType | None: The model instance if found, otherwise None.

        Raises:
            RuntimeError: If a database operation fails.
        """
        try:
            return self.session.get(self.model, id)
        except SQLAlchemyError as exc:
            self.session.rollback()
            raise RuntimeError(f"Failed to fetch {self.model.__name__} by ID {id}: {exc}") from exc

    def get_all(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        """Retrieve multiple records with pagination support.

        Args:
            skip (int): Number of records to skip. Defaults to 0.
            limit (int): Maximum number of records to return. Defaults to 100.

        Returns:
            list[ModelType]: List of retrieved model instances.

        Raises:
            RuntimeError: If a database operation fails.
        """
        try:
            stmt = select(self.model).offset(skip).limit(limit)
            return list(self.session.scalars(stmt).all())
        except SQLAlchemyError as exc:
            self.session.rollback()
            raise RuntimeError(f"Failed to fetch all {self.model.__name__} records: {exc}") from exc

    def update(self, instance_or_id: ModelType | Any, attributes: dict[str, Any]) -> ModelType | None:
        """Update an existing model instance or record identified by ID.

        Args:
            instance_or_id (ModelType | Any): Model instance or primary key ID.
            attributes (dict[str, Any]): Dictionary of attribute keys and updated values.

        Returns:
            ModelType | None: The updated and refreshed model instance, or None if not found.

        Raises:
            RuntimeError: If a database operation fails.
        """
        try:
            if isinstance(instance_or_id, self.model):
                db_obj = instance_or_id
            else:
                db_obj = self.get_by_id(instance_or_id)

            if db_obj is None:
                return None

            for key, value in attributes.items():
                if hasattr(db_obj, key):
                    setattr(db_obj, key, value)

            self.session.add(db_obj)
            self.session.commit()
            self.session.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as exc:
            self.session.rollback()
            raise RuntimeError(f"Failed to update {self.model.__name__}: {exc}") from exc

    def delete(self, instance_or_id: ModelType | Any) -> bool:
        """Delete a model instance or record identified by ID.

        Args:
            instance_or_id (ModelType | Any): Model instance or primary key ID to delete.

        Returns:
            bool: True if deleted successfully, False if record was not found.

        Raises:
            RuntimeError: If a database operation fails.
        """
        try:
            if isinstance(instance_or_id, self.model):
                db_obj = instance_or_id
            else:
                db_obj = self.get_by_id(instance_or_id)

            if db_obj is None:
                return False

            self.session.delete(db_obj)
            self.session.commit()
            return True
        except SQLAlchemyError as exc:
            self.session.rollback()
            raise RuntimeError(f"Failed to delete {self.model.__name__}: {exc}") from exc
