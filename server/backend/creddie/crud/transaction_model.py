from ..models import Transaction
from .base import CRUDBase
from ..schemas.types import UUIDType
from ..schemas.transaction_schema import CreateTransaction, UpdateTransaction


class TransactionCRUD(CRUDBase[Transaction, UUIDType, CreateTransaction, UpdateTransaction]):
    """
    Inherited CRUD class for Transaction Table.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the class."""
        super().__init__(*args, **kwargs)


transactions = TransactionCRUD(Transaction)
