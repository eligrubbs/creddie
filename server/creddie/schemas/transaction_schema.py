from typing import Optional, Annotated
from decimal import Decimal
from datetime import datetime
import csv

from pydantic import BaseModel, NaiveDatetime, ConfigDict, Field

from .types import PartyType, CurrencyType, TZType
from ..consts import MAX_DESCRIPTION_LEN


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
                "category": "Grocery",
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
    transaction_description: Annotated[str, Field(max_length=MAX_DESCRIPTION_LEN)]
    category: str

    # Optional
    is_gift: Optional[bool] = False
    gift_party: Optional[PartyType] 
    is_marketplace: Optional[bool] = False
    marketplace_party: Optional[PartyType]


    ### CSV writer/reader functions
    @classmethod
    def CSVDictWriter(cls, f) -> csv.DictWriter:
        return csv.DictWriter(
            f=f,
            fieldnames= list(cls.model_fields.keys())
        )

    @classmethod
    def CSVDictReader(cls, f) -> csv.DictReader:
        return csv.DictReader(
            f=f,
            fieldnames= list(cls.model_fields.keys())
        )
