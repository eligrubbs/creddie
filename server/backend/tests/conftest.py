from collections.abc import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport
from creddie.main import app


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
