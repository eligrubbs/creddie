import pytest
from httpx import AsyncClient, Response

@pytest.mark.anyio
async def test_app_root(client: AsyncClient):
    """Test the / GET route."""\

    resp: Response = await client.get("/")

    assert resp.json() == {"message": "Creddie says Hello!"}
