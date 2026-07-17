"""Central API router for version 1 endpoints."""

from fastapi import APIRouter

from app.api.v1.endpoints.analytics import router as analytics_router
from app.api.v1.endpoints.automations import router as automation_router
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.messages import router as messages_router
from app.api.v1.endpoints.users import router as users_router

router = APIRouter(prefix="/api/v1")

router.include_router(health_router)
router.include_router(users_router)
router.include_router(automation_router)
router.include_router(messages_router)
router.include_router(analytics_router)
