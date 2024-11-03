from decimal import Decimal
from sqlalchemy.orm import Session

from creddie.crud import transactions
from creddie.models import Transaction
from creddie.schemas.transaction_schema import CreateTransaction, UpdateTransaction
from creddie.schemas.types import CurrencyType

from ..utils.utils import num_rows_in_tbl
from ..utils.models import create_random_transaction, random_transaction_info

def test_create_transaction(sess: Session):
    rdm_txn = random_transaction_info()
    rows = num_rows_in_tbl(sess, Transaction)
    made_txn = transactions.create(sess, obj_in=rdm_txn)
    assert rows == num_rows_in_tbl(sess, Transaction) - 1
    assert sess.get(Transaction, made_txn.id) == made_txn

def test_get_transaction(sess: Session):
    rdm_txn = create_random_transaction(sess)
    txn_id = rdm_txn.id
    got_txn = transactions.get(sess, key=txn_id)

    assert got_txn == rdm_txn


def test_update_transaction(sess: Session):
    rdm_txn = create_random_transaction(sess)
    old_amount = rdm_txn.amount
    txn_id = rdm_txn.id
    update_info = UpdateTransaction(
        amount = Decimal("20.20"),
        currency = CurrencyType("USD").get(),
    )
    up_obj = transactions.update(sess, key=txn_id, obj_in=update_info)

    assert up_obj.id == txn_id
    assert up_obj.amount != old_amount
    assert up_obj.amount == "20.20"
    assert up_obj.currency == "USD"

def test_delete_transaction(sess: Session):
    rdm_txn = create_random_transaction(sess)
    txn_id = rdm_txn.id
    rows = num_rows_in_tbl(sess, Transaction)
    del_txn = transactions.delete(sess, key=txn_id)
    assert del_txn == rdm_txn
    assert rows == num_rows_in_tbl(sess, Transaction) + 1
    assert not sess.get(Transaction, txn_id)