"""Generic base service for application domain logic."""

from typing import Generic, TypeVar

RepositoryType = TypeVar("RepositoryType")


class BaseService(Generic[RepositoryType]):
    """Generic base service providing common repository context for application services.

    Attributes:
        repository (RepositoryType | None): The underlying data repository instance.
    """

    def __init__(self, repository: RepositoryType | None = None) -> None:
        """Initialize the BaseService.

        Args:
            repository (RepositoryType | None): The repository instance associated with this service.
        """
        self.repository = repository
