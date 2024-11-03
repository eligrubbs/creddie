"""Custom Pydantic types

Written here for reuse among many schemas.
"""
from typing import Any, Type, Generic, TypeVar

from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler, PositiveInt

from ..consts import (
    UUID_MAX_LEN,
    CHARS_FOR_UUID,
    CATEGORY_MAX_NAME_LEN,
    TBL_MAX_PARTY_LEN,
    TBL_MAX_CURRENCY_LEN
)


T = TypeVar("T", bound=Any)

class AbstractStrictPydanticType(Generic[T]):
    """
    Custom pydantic type that validates on creation.
    `validate` function must be defined by children classes, or you will get an error.

    Children classes are meant to be used as types. They integrate with Pydantic `BaseModel`
    to provide custom validation.

    In addition, children classes can be instantiated directly, so reliable types can be passed around.
    The internal object can be accessed via the `get` method. Validation occurs upon instantiation.

    **NOTE**: a call to `get` must be issued when doing anything that will expect the true value contained in the class. 

    Example usage in pydantic model:
    ```
    from pydantic import BaseModel, PositiveInt

    class GE50(AbstractStrictPydanticType[PositiveInt]):
        @classmethod
        def validate(cls, obj: PositiveInt):
            assert obj >= 50
            return obj

    class ExampleModel(BaseModel):
        my_num: GE50
    works = ExampleModel(my_num=55)
    errors = ExampleModel(my_num=-100)
    # Example to explain the NOTE above
    works = ExampleModel(my_num=GE50(55).get())
    errors = ExampleModel(my_num = GE50(55))
    ```

    Example usage as instantiated type:
    ```
    my_obj = GE50(500)
    assert my_obj.get() == 500
    will_error = GE50(49)
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

    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return self.obj.__str__()

    def get(self):
        return self.obj


###############
# Types Below
###############


class UUIDType(AbstractStrictPydanticType[str]):
    """UUID extended Pydantic type.
    That will fail on instatiation if incorrect.

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
    """Category Name extended Pydantic type.

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


class PartyType(AbstractStrictPydanticType[str]):
    """Transaction Party extended Pydantic type.
    Length CAN be Zero.

    Rules are:
    1. length <= `TBL_MAX_PARTY_LEN`
    2. Is not just whitespace 
    """
    @classmethod
    def validate(cls, party: str):
        assert len(party) <= TBL_MAX_PARTY_LEN
        assert not party.isspace()
        return party


class CurrencyType(AbstractStrictPydanticType[str]):
    """Transaction Party extended Pydantic type.

    Rules are:
    1. length <= `TBL_MAX_CURRENCY_LEN`
    2. length > 0
    3. Is not just whitespace
    4. only alphabetical characters
    5. must be uppercase
    """
    @classmethod
    def validate(cls, curr: str):
        assert len(curr) <= TBL_MAX_CURRENCY_LEN
        assert len(curr) > 0
        assert not curr.isspace()
        assert curr.isalpha()
        assert curr == curr.upper()
        return curr
