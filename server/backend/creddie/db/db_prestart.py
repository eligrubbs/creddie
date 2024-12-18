import asyncio
import logging

from sqlalchemy import text
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from creddie.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries_db = 60 * 1  # 1 minutes
max_tries_search = 60 * 1
wait_seconds_db = 1
wait_seconds_search = 1


@retry(
    stop=stop_after_attempt(max_tries_db),
    wait=wait_fixed(wait_seconds_db),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
async def init_db() -> None:
    """Wait for database to wake up."""
    try:
        with SessionLocal() as session:
            # Try to create session to check if DB is awake
            session.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(e)
        raise e


async def main() -> None:
    """Begin backend pre-start activities."""
    logger.info("Initializing service")
    await init_db()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    asyncio.run(main())
