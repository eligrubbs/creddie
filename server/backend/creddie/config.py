from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModeEnum(str, Enum):
    """Enumeration for possible api environment states."""

    development = "development"
    production = "production"
    testing = "testing"


class APISettings(BaseSettings):
    """Configuration Class for Creddie app."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="allow"
    )
    Mode: ModeEnum = ModeEnum.development
    DATABASE_URI: str
    ECHO_DATABASE: bool = True

    def get_db_uri_string(self) -> str:
        """Return the DB URI."""
        if self.Mode == ModeEnum.testing:
            return "sqlite:///./TestDB.db"
        return self.DATABASE_URI


settings = APISettings()
