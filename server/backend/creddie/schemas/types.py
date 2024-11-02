"""Custom Pydantic types

Written here for reuse among many schemas.
"""
from typing import Any, Type, Generic, TypeVar

from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler, PositiveInt

from ..consts import UUID_MAX_LEN, CHARS_FOR_UUID, CATEGORY_MAX_NAME_LEN


T = TypeVar("T", bound=Any)

class AbstractStrictPydanticType(Generic[T]):
    """
    Custom pydantic type that validates on creation.
    `validate` must be defined by children classes, or you will get an error.

    Children classes are meant to be used as types. They are validated on creation so they can be
    instantiated without having to add extra pydantic functions around it or add a wrapper BaseModel.

    Example usage:
    ```
    from pydantic import BaseModel, PositiveInt

    class GE50(AbstractStrictPydanticType[PositiveInt]):
        @classmethod
        def validate(cls, obj: PositiveInt):
            assert obj >= 50
            return obj

    works = GE(50)
    errors = GE(49)

    class ExampleModel(BaseModel):
        my_num: GE50
    works = ExampleModel(my_num=55)
    errors = ExampleModel(my_num=-100)
    ```

    see:  https://stackoverflow.com/a/77164254
    """
    def __new__(cls, obj: T):
        _ = cls.validate(obj)
        return super().__new__(cls)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema()
        )

    @classmethod
    def validate(cls, obj_to_validate: Any):
        raise NotImplementedError


###############
# Types Below
###############


class UUIDType(AbstractStrictPydanticType[str]):
    """
    UUID extended Pydantic type that will fail on instatiation if incorrect.

    Rules are:
    1. length == `UUID_MAX_LEN`
    2. all characters appear in `CHARS_FOR_UUID`
    """

    @classmethod
    def validate(cls, uuid: str):
        assert len(uuid) == UUID_MAX_LEN
        assert all([c in CHARS_FOR_UUID for c in uuid])
        return uuid


class CatNameType(AbstractStrictPydanticType[str]):
    """
    Category Name Type.

    Rules are:
    1. length <= `CATEGORY_MAX_NAME_LEN`
    2. length > 0
    3. Is not just whitespace
    """
    @classmethod
    def validate(cls, name: str):
        assert len(name) <= CATEGORY_MAX_NAME_LEN
        assert len(name) > 0
        assert not name.isspace()
        return name
