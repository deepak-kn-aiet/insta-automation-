from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings
from app.models.base import Base

engine = create_engine(settings.database_url, echo=settings.debug)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# TODO: Add Alembic migrations and model definitions.
