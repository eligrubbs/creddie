from pydantic import BaseModel, AwareDatetime, ConfigDict

from .types import UUIDType, CatNameType
from .metaclass import partial_model


class CreateCategory(BaseModel):
    """Info required to create a category."""
    name: CatNameType


class DeleteCategory(BaseModel):
    """Info required to delete a category."""
    id: UUIDType


class ReadCategory(BaseModel):
    """Fields returned when reading a BaseModel.
    
    This Schema should represent all the fields.
    """
    id: UUIDType
    updated_date: AwareDatetime
    created_date: AwareDatetime

    name: CatNameType


@partial_model
class UpdateCategory(BaseModel):
    """Fields able to be updated.

    """

    model_config: ConfigDict = {"extra": "forbid"}

    name: CatNameType