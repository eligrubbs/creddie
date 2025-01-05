import pathlib
import pytest
from fastapi.templating import Jinja2Templates
from jinja2 import Template
from httpx import AsyncClient, Response

creddie_dir = pathlib.Path(__file__).parent.parent.parent.resolve() / "creddie"
templates = Jinja2Templates(directory=creddie_dir / "templates")

@pytest.mark.anyio
async def test_app_root(client: AsyncClient):
    """Test the / GET route."""
    # expected_response: Template = templates.get_template(
    #     name="index.html"
    # ).render({"message": "Creddie says Hello!"})

    resp: Response = await client.get("/")

    # assert expected_response == resp.read().decode()

    assert resp.json() == {"message": "Creddie says Hello!"}
