from typing import Optional, Annotated
from decimal import Decimal

from pydantic import BaseModel, AwareDatetime, ConfigDict, Field

from .types import UUIDType, PartyType, CurrencyType
from .metaclass import partial_model
from ..consts import TBL_MAX_DESC_LEN


class CreateTransaction(BaseModel):
    """Info required to create a transaction."""
    amount: Annotated[Decimal, Field(decimal_places=2)]
    currency: CurrencyType
    is_credit: bool
    transaction_date: AwareDatetime

    other_party: PartyType
    transaction_description: Annotated[str, Field(max_length=TBL_MAX_DESC_LEN)]
    category_id: UUIDType

    # Optional
    is_gift: Optional[bool] = False
    gift_party: Optional[PartyType] 
    is_marketplace: Optional[bool] = False
    marketplace_party: Optional[PartyType] 


class ReadTransaction(BaseModel):
    """Info returned when reading a transaction."""
    id: UUIDType
    updated_date: AwareDatetime
    created_date: AwareDatetime

    amount: Annotated[Decimal, Field(decimal_places=2)]
    currency: CurrencyType
    is_credit: bool
    transaction_date: AwareDatetime

    other_party: PartyType
    transaction_description: Annotated[str, Field(max_length=TBL_MAX_DESC_LEN)]
    category_id: UUIDType

    # Optional
    is_gift: Optional[bool] = False
    gift_party: Optional[PartyType]
    is_marketplace: Optional[bool] = False
    marketplace_party: Optional[PartyType]


@partial_model
class UpdateTransaction(BaseModel):
    """Info in a transaction able to be updated."""
    amount: Annotated[Decimal, Field(decimal_places=2)]
    currency: CurrencyType
    is_credit: bool
    transaction_date: AwareDatetime

    other_party: PartyType
    transaction_description: Annotated[str, Field(max_length=TBL_MAX_DESC_LEN)]
    category_id: UUIDType

    is_gift: bool
    gift_party: PartyType
    is_marketplace: bool
    marketplace_party: PartyType
