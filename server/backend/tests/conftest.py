from collections.abc import AsyncGenerator, Generator
import random

import pytest
from httpx import AsyncClient, ASGITransport
from creddie.main import app

# Random seed
random.seed(10)

@pytest.fixture
def anyio_backend() -> str:
    """Clarify asyncio as backend for all pytest.mark.anyio decorators."""
    return "asyncio"


@pytest.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Return an AsyncClient of the application."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="https://test/"
    ) as c:
        yield c

# Create Test Database and provide it as a fixture
from creddie.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

connect_args = {"check_same_thread": False}
engine = create_engine(url = settings.get_db_uri_string(),
                       connect_args=connect_args,
                       echo=False,
                    )

SessionLocal: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_= Session,
    expire_on_commit=False,
)

@pytest.fixture
def sess() -> Generator[Session, None]:
    """
    SQLite session generator.
    """
    with SessionLocal() as session:
        yield session
