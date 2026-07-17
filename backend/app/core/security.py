"""Simple security helpers for encrypting and decrypting values."""

from cryptography.fernet import Fernet

from app.core.config import get_settings


class SecurityService:
    def __init__(self) -> None:
        settings = get_settings()
        self.secret = settings.jwt_secret.encode("utf-8")
        self.fernet = Fernet(self.secret[:32].ljust(32, b"0"))

    def encrypt(self, value: str) -> str:
        return self.fernet.encrypt(value.encode("utf-8")).decode("utf-8")

    def decrypt(self, value: str) -> str:
        return self.fernet.decrypt(value.encode("utf-8")).decode("utf-8")
