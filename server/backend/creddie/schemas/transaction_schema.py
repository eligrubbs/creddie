from typing import Optional, Annotated
from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, NaiveDatetime, ConfigDict, Field

from .types import UUIDType, PartyType, CurrencyType, TZType
from .metaclass import partial_model
from ..consts import TBL_MAX_DESC_LEN


class CreateTransaction(BaseModel):
    """Info required to create a transaction."""
    model_config: ConfigDict = {
        "json_schema_extra": {
            "examples": [{
                "amount": "20.0",
                "currency": "USD",
                "is_credit": True,
                "transaction_date": datetime.now(),
                "transaction_tz": "America/New_York",
                "other_party": "Walmart",
                "transaction_description": "a transaction.",
                "category_id": "REQUIRED",
                "is_gift": False,
                "gift_party": "",
                "is_marketplace": False,
                "marketplace_party": ""
            }]
        }
    }

    amount: Annotated[Decimal, Field(decimal_places=2, gt=0)]
    currency: CurrencyType
    is_credit: bool
    transaction_date: NaiveDatetime
    transaction_tz: TZType

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
    updated_at: NaiveDatetime
    created_at: NaiveDatetime

    amount: Annotated[Decimal, Field(decimal_places=2, gt=0)]
    currency: CurrencyType
    is_credit: bool
    transaction_date: NaiveDatetime
    transaction_tz: str

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

    model_config: ConfigDict = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [{
                "amount": "20.0",
                "currency": "USD",
                "is_credit": True,
                "transaction_date": datetime.now(),
                "transaction_tz": "America/New_York",
                "other_party": "Walmart",
                "transaction_description": "a transaction.",
                "category_id": "REQUIRED",
                "is_gift": False,
                "gift_party": "",
                "is_marketplace": False,
                "marketplace_party": ""
            }]
        }
    }

    amount: Annotated[Decimal, Field(decimal_places=2, gt=0)]
    currency: CurrencyType
    is_credit: bool
    transaction_date: NaiveDatetime
    transaction_tz: str

    other_party: PartyType
    transaction_description: Annotated[str, Field(max_length=TBL_MAX_DESC_LEN)]
    category_id: UUIDType

    is_gift: bool
    gift_party: PartyType
    is_marketplace: bool
    marketplace_party: PartyType
