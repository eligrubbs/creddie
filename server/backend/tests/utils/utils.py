
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

def num_rows_in_tbl(db: Session, table: type[DeclarativeBase]):
    """Return number of rows in passed in table."""
    num_rows = -1
    num_rows = db.execute(select(func.count()).select_from(table))
    return num_rows.scalar()
