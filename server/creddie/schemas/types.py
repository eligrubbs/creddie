"""Custom Pydantic types

Written here for reuse among many schemas.
"""
from typing import Any, Type, Generic, TypeVar
from zoneinfo import ZoneInfo

from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler

from ..consts import MAX_PARTY_LEN, MAX_CURRENCY_LEN

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
            if obj < 50:
                raise ValueError("value must be >= 50")
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

class PartyType(AbstractStrictPydanticType[str]):
    """Transaction Party extended Pydantic type.
    Length CAN be Zero.

    Rules are:
    1. length <= `MAX_PARTY_LEN`
    2. Is not just whitespace 
    3. No leading/trailing whitespace
    """
    @classmethod
    def validate(cls, party: str):
        if len(party) > MAX_PARTY_LEN:
            raise ValueError(f"Party should be <= {MAX_PARTY_LEN} chars long")
        if party.isspace():
            raise ValueError(f"Party can't be only whitespace")
        if not party.strip() == party:
            raise ValueError(f"Party can't have leading/trailing whitespace")
        return party


class CurrencyType(AbstractStrictPydanticType[str]):
    """Transaction Party extended Pydantic type.

    Rules are:
    1. length <= `MAX_CURRENCY_LEN`
    2. length > 0
    3. Is not just whitespace
    4. only alphabetical characters
    5. must be uppercase
    6. No leading/trailing whitespace
    """
    @classmethod
    def validate(cls, curr: str):
        if len(curr) > MAX_CURRENCY_LEN:
            raise ValueError(f"Currency must be <= {MAX_CURRENCY_LEN} chars long")
        if len(curr) <= 0:
            raise ValueError(f"Currency must be > 0 chars long")
        if curr.isspace():
            raise ValueError(f"Currency can't be only whitespace")
        if not curr.isalpha():
            raise ValueError(f"Currency must only contain alphabetical characters")
        if curr != curr.upper():
            raise ValueError(f"Currency must only contain capital letters")
        if not curr.strip() == curr:
            raise ValueError(f"Currency can't have leading/trailing whitespace")
        return curr
    
class TZType(AbstractStrictPydanticType[str]):
    """Timezone name extended Pydantic Type.

    Rules are:
    1. Is a valid timezone key in an IANA Timezone Database
    
    The following should not raise an error:
    ```
    from zoneinfo import ZoneInfo
    my_tz = "America/Los_Angeles"
    no_err_zone = ZoneInfo(my_tz)
    ```
    """
    @classmethod
    def validate(cls, tz: str):
        ZoneInfo(tz)
        return tz
