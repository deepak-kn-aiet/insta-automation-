"""Service for Analytics domain operations."""

from app.repositories.analytics_repository import AnalyticsRepository
from app.services.base import BaseService


class AnalyticsService(BaseService[AnalyticsRepository]):
    """Service handling operations for the Analytics domain."""

    def __init__(self, repository: AnalyticsRepository | None = None) -> None:
        """Initialize AnalyticsService with an AnalyticsRepository.

        Args:
            repository (AnalyticsRepository | None): AnalyticsRepository instance.
        """
        super().__init__(repository=repository)
