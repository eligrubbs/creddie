"""
File to handle configuration of Creddie
"""
import pathlib

from typing_extensions import Annotated, Doc
from pydantic import field_validator, ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    """Configuration Class for Creddie app."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="allow",
    )

    PATH_TO_CSV_FILE: Annotated[
        str,
        Doc(
            """
            Path to the CSV file that creddie should read from
            """
        )
    ]
    FORM_ACCESS_KEY: Annotated[
        str,
        Doc(
            """
            Without this key, all GET requests to the form or log_transaction endpoints will result in 401 Unauthorized.
            """
        )
    ]

    @field_validator("PATH_TO_CSV_FILE", mode="before")
    @classmethod
    def file_is_csv(cls, v: str):
        if (v == ""):
            raise ValueError("path can't be empty")
        if (v[-4:] != ".csv"):
            raise ValueError('path does not end in ".csv"')
        return v

    def csv_abs_path(self):
        """
        Returns the path object of `PATH_TO_CSV_FILE` after calling `.resolve(strict=False)` to get the absolute path.

        Calling this method does not imply that the path actually exists.
        """
        return pathlib.Path(self.PATH_TO_CSV_FILE).resolve()


settings = APISettings()
