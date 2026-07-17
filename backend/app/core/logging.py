"""Reusable logging helpers for the backend application."""

import logging
import sys
from datetime import datetime, timezone
from typing import Any


def configure_logging() -> logging.Logger:
    logger = logging.getLogger("instagram_assistant")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)

    return logger


def get_logger() -> logging.Logger:
    return configure_logging()


def build_log_payload(method: str, path: str, status_code: int, execution_time: float) -> dict[str, Any]:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": method,
        "path": path,
        "status_code": status_code,
        "execution_time_ms": round(execution_time * 1000, 3),
    }
