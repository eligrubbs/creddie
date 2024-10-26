"""
This file contains a table that exists only so I can get stuff set up.

This file and all mentions of this table will be deleted later.

Copied from: https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/
"""

from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
