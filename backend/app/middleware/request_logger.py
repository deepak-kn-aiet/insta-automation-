"""Middleware that logs request metadata for observability."""

import time
from typing import Any, Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from app.core.logging import build_log_payload, get_logger

logger = get_logger()


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Any]) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        execution_time = time.perf_counter() - start_time
        payload = build_log_payload(request.method, request.url.path, response.status_code, execution_time)
        logger.info("request_completed", extra=payload)
        return response
