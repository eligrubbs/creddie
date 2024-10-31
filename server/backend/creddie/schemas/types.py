"""Custom Pydantic types

Written here for reuse among many schemas.
"""
from typing_extensions import Annotated
from pydantic import Field

from ..consts import UUID_MAX_LEN, CATEGORY_MAX_NAME_LEN

UUIDType = Annotated[str, Field(min_length=UUID_MAX_LEN, max_length=UUID_MAX_LEN)]


# Category
CatNameType = Annotated[str, Field(min_length=0, max_length=CATEGORY_MAX_NAME_LEN)]
