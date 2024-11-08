"""
Transaction Category Model.
"""
from sqlalchemy import Column, String, DateTime

from ..utils.tools import get_UUID, utc_now_naive
from . import Base
from ..consts import UUID_MAX_LEN, CATEGORY_MAX_NAME_LEN

class TxnCategory(Base):
    __tablename__ = "txncategories"

    # Enriched
    id = Column(String(UUID_MAX_LEN), default=get_UUID, nullable=False, primary_key=True, unique=True)
    updated_at = Column(DateTime, default=utc_now_naive, onupdate=utc_now_naive, nullable=False)
    created_at = Column(DateTime, default=utc_now_naive, nullable=False)

    # Required
    name = Column(String(CATEGORY_MAX_NAME_LEN), nullable=False, unique=True)
