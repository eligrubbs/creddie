from sqlalchemy.orm import Session

from creddie.models import TxnCategory
from creddie.utils.tools import get_UUID

def random_category_name():
    return f"Category {get_UUID()}"

def create_random_category(sess: Session):
    cat = TxnCategory(name=random_category_name())
    sess.add(cat)
    sess.commit()
    sess.refresh(cat)
    return cat
