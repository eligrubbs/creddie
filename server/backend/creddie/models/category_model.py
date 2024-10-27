"""
Transaction Category Model.
"""
from sqlalchemy import Column, String, TIMESTAMP

from ..utils.tools import get_8_digit_UUID, utc_now
from . import Base

class TxnCategory(Base):
    __tablename__ = "txncategories"

    # Enriched
    id = Column(String(8), default=get_8_digit_UUID, nullable=False, primary_key=True, unique=True)
    updated_date = Column(TIMESTAMP(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), default=utc_now, nullable=False)

    # Required
    name = Column(String(32), nullable=False)
