import pytest
from httpx import AsyncClient, Response


@pytest.mark.anyio
async def test_app_root(client: AsyncClient):
    """Test the / GET route."""
    expected_json = {"message": "Creddie says Hello!"}
    resp: Response = await client.get("/")

    assert expected_json == resp.json()
