from sqlalchemy.orm import Session

from creddie.schemas.category_schema import CreateCategory
from creddie.models.category_model import TxnCategory
from creddie.crud.category_crud import categories

from ..utils import num_rows_in_tbl
from ..utils.models import random_category_name

def test_create_category(sess: Session):
    rows = num_rows_in_tbl(sess, TxnCategory)

    create_data = CreateCategory(name=random_category_name())
    obj = categories.create(sess, obj_in = create_data)

    rows_after = num_rows_in_tbl(sess, TxnCategory)
    assert rows+1 == rows_after

    #assert sess.get(TxnCategory, obj.id) == obj

