"""
This file contains a table that exists only so I can get stuff set up.

This file and all mentions of this table will be deleted later.

Copied from: https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/
"""
from sqlalchemy import Column, String, Integer
from . import Base

class Hero(Base):
    __tablename__ = "Heros"

    id = Column(Integer, default=None, primary_key=True)
    name = Column(String, index=True)
    secret_name = Column(String)
    age = Column(Integer, default=None, index=True)
