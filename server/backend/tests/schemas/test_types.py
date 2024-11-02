"""
Test custom Pydantic types.
"""
import pytest
from pydantic import BaseModel

from creddie.schemas.types import UUIDType, CatNameType
from creddie.consts import CATEGORY_MAX_NAME_LEN

# UUID
def test_create_uuid_type():
    bob = UUIDType("OOOOO452")
    bob = UUIDType("12345678")

def test_catches_bad_create_uuid_type():
    with pytest.raises(Exception):
        bob = UUIDType("badUUID")
    with pytest.raises(Exception):
        bob = UUIDType("TOOLONG22")
    with pytest.raises(Exception):
        bob = UUIDType("SHORT")
    with pytest.raises(Exception):
        bob = UUIDType("BADCHAR!")
    with pytest.raises(Exception):
        bob = UUIDType("")

def test_uuid_works_pydantic_model():
    class Dumb(BaseModel):
        uuuu: UUIDType
    uuid = "UIRUE231"
    bob = Dumb(uuuu=uuid)
    assert {"uuuu": uuid} == bob.model_dump()

def test_uuid_pydantic_model_error():
    class Dumb(BaseModel):
        uuuu: UUIDType
    with pytest.raises(Exception):
        bob = Dumb(uuuu= "UIRUE231!")


# Category
def test_create_category_name():
    CatNameType("category")
    CatNameType("gggggggggggggggggggggggggggggggg") # 32
    CatNameType("@#%$#W")

def test_catches_bad_cat_create():
    with pytest.raises(Exception):
        CatNameType("")
    with pytest.raises(Exception):
        CatNameType("ggggggggggggggggggggggggggggggggg") # 33
    with pytest.raises(Exception):
        CatNameType("         ")

def test_category_works_pydantic_model():
    class Dumb(BaseModel):
        uuuu: CatNameType
    catname = "My Cool Category!!!"
    bob = Dumb(uuuu=catname)
    assert {"uuuu": catname} == bob.model_dump()

def test_category_pydantic_model_error():
    class Dumb(BaseModel):
        uuuu: CatNameType
    with pytest.raises(Exception):
        bob = Dumb(uuuu= "      ")
