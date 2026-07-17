"""Dependency injection scaffolding for the API layer."""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal


def get_db() -> Session:
    """Provide a database session dependency placeholder."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DBSessionDependency = Annotated[Session, Depends(get_db)]
