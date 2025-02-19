"""
File to handle configuration of Creddie
"""

from typing_extensions import Annotated, Doc
from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    """Configuration Class for Creddie app."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="allow",
    )

    FORM_ACCESS_KEY: Annotated[
        str,
        Doc(
            """
            Without this key, all GET requests to the form or log_transaction endpoints will result in 401 Unauthorized.
            """
        )
    ]


settings = APISettings()
