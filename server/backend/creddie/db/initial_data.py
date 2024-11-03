"""Fill database with initial data, if it isn't already present.

Initial Data:
1. Input the pre-specified list of categories.
"""
import asyncio
import logging

from sqlalchemy.orm import Session

from creddie.db.session import SessionLocal
from creddie.schemas.types import CatNameType
from creddie.schemas.category_schema import CreateCategory
from creddie.crud import categories
from creddie.consts import INITIAL_CATEGORIES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init_categories(sess: Session):
    """Load initial categories into the table."""

    cats_in_db = categories.get_all_names(sess)
    if not cats_in_db:
        logger.info("No Categories found at startup. Loading defaults...")
        for cat in INITIAL_CATEGORIES:
            create = CreateCategory(name = cat)
            categories.create(sess, obj_in=create)
        cats_in_db = categories.get_all_names(sess)
        assert cats_in_db == set(INITIAL_CATEGORIES)
    else:
        logger.info("Categories found at startup.")


async def init() -> None:
    """Wrap loading initial db."""
    with SessionLocal() as sess:
        await init_categories(sess)


async def main() -> None:
    """Begin loading initial data."""
    logger.info("Creating initial data")
    await init()
    logger.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(main())
