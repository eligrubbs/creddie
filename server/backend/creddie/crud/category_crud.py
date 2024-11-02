from ..models import TxnCategory
from .base import CRUDBase
from ..schemas.types import UUIDType
from ..schemas.category_schema import CreateCategory, UpdateCategory


class CategoryCRUD(CRUDBase[TxnCategory, UUIDType, CreateCategory, UpdateCategory]):
    """
    Inherited CRUD class for TxnCategory Table.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the class."""
        super().__init__(*args, **kwargs)


categories = CategoryCRUD(TxnCategory)
