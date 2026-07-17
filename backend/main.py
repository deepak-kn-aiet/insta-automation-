import os
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BACKEND_ROOT = Path(__file__).resolve().parent
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.api.v1.router import router as api_v1_router
from app.core.config import get_settings
from app.middleware.error_handler import ExceptionHandlingMiddleware
from app.middleware.request_logger import RequestLoggingMiddleware

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.app_version)

origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(ExceptionHandlingMiddleware)

app.include_router(api_v1_router)


class HealthResponse(BaseModel):
    status: str
    app: str


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "app": "instagram-assistant",
        "version": settings.app_version,
        "status": "running",
    }


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", app=settings.app_name)
