from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import TxnCategory
from .base import CRUDBase
from ..schemas.types import UUIDType, CatNameType
from ..schemas.category_schema import CreateCategory, UpdateCategory


class CategoryCRUD(CRUDBase[TxnCategory, UUIDType, CreateCategory, UpdateCategory]):
    """
    Inherited CRUD class for TxnCategory Table.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the class."""
        super().__init__(*args, **kwargs)


    def get_by_name(self, sess: Session, *, name: CatNameType | str) -> TxnCategory:
        if isinstance(name, str):
            name = CatNameType(name)
        get_stmt = select(self.model).where(getattr(self.model, "name") == name.get())
        result = sess.execute(get_stmt)
        return result.scalar_one_or_none()

    def get_all_names(self, sess: Session) -> set:
        stmt = select(self.model.name).order_by(self.model.created_date)
        result = sess.execute(stmt)
        return set(result.scalars().all())
        

categories = CategoryCRUD(TxnCategory)
