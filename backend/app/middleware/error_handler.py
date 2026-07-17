"""Middleware that handles unexpected exceptions consistently."""

import traceback
from datetime import datetime, timezone

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import get_logger

logger = get_logger()


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except RequestValidationError as exc:
            return JSONResponse(status_code=422, content={"detail": exc.errors()})
        except Exception as exc:  # noqa: BLE001
            timestamp = datetime.now(timezone.utc).isoformat()
            stack_trace = traceback.format_exc()
            logger.exception(
                "Unhandled exception | timestamp=%s | method=%s | path=%s | stack_trace=%s",
                timestamp,
                request.method,
                request.url.path,
                stack_trace,
            )
            return JSONResponse(status_code=500, content={"detail": "internal_server_error"})
