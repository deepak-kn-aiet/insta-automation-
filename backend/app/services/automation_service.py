from typing import Any


class AutomationService:
    def __init__(self) -> None:
        # TODO: Inject repositories and AI provider adapters.
        pass

    def get_status(self) -> dict[str, Any]:
        return {
            "status": "initialized",
            "feature": "keyword-based automation",
            "ai_enabled": False,
        }
