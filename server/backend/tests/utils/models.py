from sqlalchemy.orm import Session
from pydantic import AwareDatetime

from creddie.schemas.types import PartyType, UUIDType
from creddie.schemas.transaction_schema import CreateTransaction
from creddie.models import TxnCategory, Transaction
from creddie.utils.tools import get_UUID, utc_now_naive

# Category
def random_category_name():
    return f"Category {get_UUID()}"

def create_random_category(sess: Session):
    cat = TxnCategory(name=random_category_name())
    sess.add(cat)
    sess.commit()
    sess.refresh(cat)
    return cat


# Transaction
def random_transaction_info() -> CreateTransaction:
    return CreateTransaction(**{
        "amount": 200.20,
        "currency": "USD",
        "is_credit": False,
        "transaction_date": utc_now_naive(),
        "other_party": PartyType(f"Other Party {get_UUID()}").get(),
        "transaction_description": f"{get_UUID()*3}",
        "category_id": UUIDType(get_UUID()).get(),
        "is_gift": False,
        "gift_party": PartyType(f"Gift Party {get_UUID()}").get(),
        "is_marketplace": False,
        "marketplace_party": PartyType(f"Marketplace {get_UUID()}").get(),
    })

def create_random_transaction(sess: Session):
    txn = Transaction(**random_transaction_info().model_dump())
    sess.add(txn)
    sess.commit()
    sess.refresh(txn)
    return txn
