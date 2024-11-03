"""
Transaction Data Model.
"""
from sqlalchemy import Column, String, Numeric, Boolean, TIMESTAMP, ForeignKey

from ..utils.tools import get_UUID, utc_now
from . import Base
from .category_model import TxnCategory
from ..consts import UUID_MAX_LEN, TBL_MAX_PARTY_LEN, TBL_MAX_CURRENCY_LEN, TBL_AMOUNT_DECIMAL_POINTS, TBL_MAX_DESC_LEN

class Transaction(Base):
    __tablename__ = "transactions"

    # Enriched
    id = Column(String(UUID_MAX_LEN), default=get_UUID, nullable=False, primary_key=True, unique=True)
    updated_date = Column(TIMESTAMP(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), default=utc_now, nullable=False)

    # Required
    amount = Column(Numeric(scale=TBL_AMOUNT_DECIMAL_POINTS), nullable=False)
    currency = Column(String(TBL_MAX_CURRENCY_LEN), nullable=False)
    is_credit = Column(Boolean, nullable=False)
    transaction_date = Column(TIMESTAMP(timezone=True), nullable=False)

    other_party = Column(String(TBL_MAX_PARTY_LEN), nullable=False)
    transaction_description = Column(String(TBL_MAX_DESC_LEN), nullable=False)
    category_id = Column(String(UUID_MAX_LEN), ForeignKey(TxnCategory.id), nullable=False)

    # Optional
    is_gift = Column(Boolean, default=False, nullable=False)
    gift_party = Column(String(TBL_MAX_PARTY_LEN), nullable=False, default="")
    is_marketplace = Column(Boolean, default=False, nullable=False)
    marketplace_party = Column(String(TBL_MAX_PARTY_LEN), nullable=False, default="")
