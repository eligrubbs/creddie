from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    """Configuration Class for Creddie app."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="allow"
    )

    DATABASE_URI: str
    ECHO_DATABASE: bool = True

    def get_db_uri_string(self) -> str:
        """Return the DB URI."""
        return self.DATABASE_URI


settings = APISettings()
