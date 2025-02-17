"""
Handle prestart actions.

1. Make sure that there exists a CSV at `PATH_TO_CSV_FILE` otherwise create a blank csv

"""
import os
import pathlib
import asyncio
import logging

from creddie.config import settings
from creddie.schemas.transaction_schema import CreateTransaction

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def check_for_csv(the_path: pathlib.Path) -> None:
    """
    Look for a csv at the path in the variable `PATH_TO_CSV_FILE`
    """
    if the_path.exists():
        logger.info(f"Found: {the_path}")
    else:
        # Create new csv file and write header
        if not (the_path.parent.exists()):
            os.makedirs(the_path.parent)
        with open(the_path, 'w') as csvfile:
            # If here, the file should have just been made, and therefore is empty
            assert(os.stat(the_path).st_size == 0)

            writer = CreateTransaction.CSVDictWriter(csvfile)
            writer.writeheader()
        logger.info(f"Created: {the_path}")


async def main() -> None:
    """Entrypoint for startup task."""
    the_path = settings.csv_abs_path()
    logger.info(f"Scanning for csv at: {the_path}")
    await check_for_csv(the_path)
    logger.info(f"CSV ready for read/write at: {the_path}")


if __name__ == "__main__":
    asyncio.run(main())
