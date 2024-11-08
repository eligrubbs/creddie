"""
Dependencies for API Routes.
"""
from typing import Generator, Annotated
from sqlalchemy.orm import Session
from fastapi import Depends

from ..db.session import SessionLocal


def get_db_session() -> Generator[Session, None, None]:
    """Yield a connection to the database."""
    with SessionLocal() as sess:
        yield sess


SessDep = Annotated[Session, Depends(get_db_session)]
