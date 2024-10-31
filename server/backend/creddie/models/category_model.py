"""
Transaction Category Model.
"""
from sqlalchemy import Column, String, TIMESTAMP

from ..utils.tools import get_UUID, utc_now
from . import Base
from ..consts import UUID_MAX_LEN, CATEGORY_MAX_NAME_LEN

class TxnCategory(Base):
    __tablename__ = "txncategories"

    # Enriched
    id = Column(String(UUID_MAX_LEN), default=get_UUID, nullable=False, primary_key=True, unique=True)
    updated_date = Column(TIMESTAMP(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), default=utc_now, nullable=False)

    # Required
    name = Column(String(CATEGORY_MAX_NAME_LEN), nullable=False, unique=True)
