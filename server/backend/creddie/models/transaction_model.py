"""
Transaction Data Model.
"""
from sqlalchemy import Column, String, Numeric, Boolean, TIMESTAMP, ForeignKey

from ..utils.tools import get_8_digit_UUID, utc_now
from . import Base
from .category_model import TxnCategory

class Transaction(Base):
    __tablename__ = "transactions"

    # Enriched
    id = Column(String(8), default=get_8_digit_UUID, nullable=False, primary_key=True, unique=True)
    updated_date = Column(TIMESTAMP(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)
    entry_date = Column(TIMESTAMP(timezone=True), default=utc_now, nullable=False)

    # Required
    amount = Column(Numeric(scale=2), nullable=False)
    currency = Column(String(4), nullable=False)
    is_credit = Column(Boolean, nullable=False)
    transaction_date = Column(TIMESTAMP(timezone=True), nullable=False)

    other_party = Column(String(64), nullable=False)
    transaction_description = Column(String(256), nullable=False)
    category_id = Column(String(8), ForeignKey(TxnCategory.id), nullable=False)

    # Optional
    is_gift = Column(Boolean, default=False, nullable=False)
    gift_party = Column(String(64), nullable=False, default="")
    is_marketplace = Column(Boolean, default=False, nullable=False)
    marketplace_party = Column(String(64), nullable=False, default="")