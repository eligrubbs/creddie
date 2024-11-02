from sqlalchemy.orm import Session

from creddie.schemas.category_schema import CreateCategory, UpdateCategory
from creddie.models.category_model import TxnCategory
from creddie.crud import categories

from ..utils import num_rows_in_tbl
from ..utils.models import (
    random_category_name,
    create_random_category
)

def test_create_category(sess: Session):
    rows = num_rows_in_tbl(sess, TxnCategory)

    create_data = CreateCategory(name=random_category_name())
    obj = categories.create(sess, obj_in = create_data)

    rows_after = num_rows_in_tbl(sess, TxnCategory)

    assert rows+1 == rows_after
    assert sess.get(TxnCategory, obj.id) == obj

def test_get_category(sess: Session):
    rdm_cat = create_random_category(sess)
    get_cat = categories.get(sess, key=rdm_cat.id)

    assert rdm_cat == get_cat

def test_update_category(sess: Session):
    rdm_cat = create_random_category(sess)
    old_id = rdm_cat.id
    update_name = "Cool Name"
    assert rdm_cat.name != update_name
    update_info = UpdateCategory(name=update_name)

    update_cat = categories.update(sess, key=old_id, obj_in=update_info)

    assert update_cat.name == update_name
    assert update_cat.id == old_id

def test_delete_category(sess: Session):
    rdm_cat = create_random_category(sess)
    cat_id = rdm_cat.id
    rows = num_rows_in_tbl(sess, TxnCategory)

    deleted_cat = categories.delete(sess, key=cat_id)

    assert rows == num_rows_in_tbl(sess, TxnCategory) + 1
    assert deleted_cat == rdm_cat
