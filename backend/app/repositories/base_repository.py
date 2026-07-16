from typing import Generic, TypeVar

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self) -> None:
        # TODO: Inject database session and implement CRUD helpers.
        pass
