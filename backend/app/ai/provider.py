class AIProvider:
    def __init__(self) -> None:
        # TODO: Implement Ollama and Gemini adapters behind feature flags.
        self.enabled = False

    def generate_reply(self, message: str) -> str:
        return f"AI reply placeholder for: {message}"
