"""
Test custom Pydantic types.
"""
import pytest
from pydantic import BaseModel

from creddie.schemas.types import UUIDType, CatNameType, PartyType, CurrencyType
from creddie.consts import CATEGORY_MAX_NAME_LEN

# UUID
def test_create_uuid_type():
    UUIDType("OOOOO452")
    UUIDType("12345678")

def test_catches_bad_create_uuid_type():
    with pytest.raises(Exception):
        UUIDType("badUUID")
    with pytest.raises(Exception):
        UUIDType("TOOLONG22")
    with pytest.raises(Exception):
        UUIDType("SHORT")
    with pytest.raises(Exception):
        UUIDType("BADCHAR!")
    with pytest.raises(Exception):
        UUIDType("")

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


# Transaction Party
def test_create_party_name():
    PartyType("party name")
    PartyType("gggggggggggggggggggggggggggggggg") # 32
    PartyType("@#%$#W")
    PartyType("")

def test_catches_bad_party_create():
    with pytest.raises(Exception):
        PartyType("ggggggggggggggggggggggggggggggggg") # 33
    with pytest.raises(Exception):
        PartyType(" ")

def test_party_works_pydantic_model():
    class Dumb(BaseModel):
        uuuu: PartyType
    partyname = "I paid this person!!!"
    bob = Dumb(uuuu=partyname)
    assert {"uuuu": partyname} == bob.model_dump()

def test_party_pydantic_model_error():
    class Dumb(BaseModel):
        uuuu: PartyType
    with pytest.raises(Exception):
        bob = Dumb(uuuu= "      ")


# Transaction Currency
def test_create_currency_name():
    CurrencyType("CURR")
    CurrencyType("BLB") # 
    CurrencyType("IU")
    CurrencyType("U")

def test_catches_bad_currency_create():
    with pytest.raises(Exception):
        CurrencyType("GGGGG") # 5
    with pytest.raises(Exception):
        CurrencyType("")
    with pytest.raises(Exception):
        CurrencyType("USD!")
    with pytest.raises(Exception):
        CurrencyType("US D")
    with pytest.raises(Exception):
        CurrencyType("usd")

def test_currency_works_pydantic_model():
    class Dumb(BaseModel):
        uuuu: CurrencyType
    currencyname = "USD"
    bob = Dumb(uuuu=currencyname)
    assert {"uuuu": currencyname} == bob.model_dump()

def test_currency_pydantic_model_error():
    class Dumb(BaseModel):
        uuuu: CurrencyType
    with pytest.raises(Exception):
        bob = Dumb(uuuu= "      ")
