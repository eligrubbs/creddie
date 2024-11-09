from sqlalchemy import delete
from sqlalchemy.orm import Session

from creddie.schemas.category_schema import CreateCategory, UpdateCategory
from creddie.schemas.types import CatNameType
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

def test_get_by_name(sess: Session):
    rdm_cat = create_random_category(sess)
    rdm_name = rdm_cat.name

    obj = categories.get_by_name(sess, name=CatNameType(rdm_name))
    assert obj.id == rdm_cat.id
    obj2 = categories.get_by_name(sess, name=rdm_name)
    assert obj2.id == rdm_cat.id

def test_get_all_names(sess: Session):
    # Remove all categories from previous tests
    sess.execute(delete(TxnCategory))
    names = []
    for _ in range(5):
        rdm_cat = create_random_category(sess)
        names.append(rdm_cat.name)
    db_names = categories.get_all_names(sess)
    assert not set(names).difference(db_names)


def test_get_all(sess: Session):
    # Remove all categories from previous tests
    sess.execute(delete(TxnCategory))
    dudes = []
    for _ in range(5):
        rdm_cat = create_random_category(sess)
        dudes.append(rdm_cat)
    db_names = categories.get_all(sess)
    assert not set(dudes).difference(db_names)