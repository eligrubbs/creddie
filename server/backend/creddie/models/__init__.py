"""Import all models here.

Important because alembic will be pointed to this file to collect metadata on all the tables we have.
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Declarative Base class."""

    pass


from .example_model import Hero
from .transaction_model import Transaction
