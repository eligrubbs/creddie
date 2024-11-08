from pydantic import BaseModel, NaiveDatetime, ConfigDict

from .types import UUIDType, CatNameType
from .metaclass import partial_model


class CreateCategory(BaseModel):
    """Info required to create a category."""
    name: CatNameType


class ReadCategory(BaseModel):
    """Fields returned when reading a BaseModel.
    
    This Schema should represent all the fields.
    """
    id: UUIDType
    updated_at: NaiveDatetime
    created_at: NaiveDatetime

    name: CatNameType


@partial_model
class UpdateCategory(BaseModel):
    """Fields able to be updated.

    """

    model_config: ConfigDict = {"extra": "forbid"}

    name: CatNameType
