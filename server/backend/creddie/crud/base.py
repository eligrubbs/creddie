"""
Reusable class that contains ONLY basic CRUD functions.
"""
from typing import TypeVar, Generic

from sqlalchemy import update
from sqlalchemy.orm import DeclarativeBase, Session
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from ..schemas.types import AbstractStrictPydanticType


ModelType = TypeVar("ModelType", bound=DeclarativeBase)

PrimaryKeySchemaType = TypeVar("PrimaryKeySchemaType", BaseModel, AbstractStrictPydanticType)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, PrimaryKeySchemaType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: ModelType):
        """Interhitable baseclass that provides CRUD methods for `model`.

        Parameters:
        `model`: A SQLAlchemy DeclaritiveBase class that this CRUDBase class adds functionality to.
        
        Associated Types:
        `ModelType`: A SQLAlchemy DeclaritiveBase class that this CRUDBase class adds functionality to.
        `PrimaryKeySchemaType: Custom Pydantic BaseModel that contains name of primary key fields and their types
            Included because we shouldn't assume every table has a single field as their primary key.

        """
        self.model = model

    def create(self, sess: Session, *, obj_in: CreateSchemaType) -> ModelType:

        obj_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_data)
        sess.add(db_obj)
        sess.commit()
        sess.refresh(db_obj)
        return db_obj

    def get(self, sess: Session, *, key: PrimaryKeySchemaType) -> ModelType | None:

        if isinstance(key, BaseModel):
            key = key.model_dump()
        return sess.get(self.model, key)

    def update(self, sess: Session, *, key: PrimaryKeySchemaType, obj_in: UpdateSchemaType) -> ModelType | None:

        obj_to_update = self.get(sess, key=key)
        if not obj_to_update:
            return None

        update_stmt = update( self.model )
        if isinstance(key, BaseModel):
            for column, val in key.model_dump().items():
                update_stmt = update_stmt.where(getattr(self.model, column) == val)
        else:
            update_stmt = update_stmt.where(self.model.id == key)
    
        update_stmt = update_stmt.values(**(obj_in.model_dump(exclude_unset=True)) )

        sess.execute(update_stmt)
        sess.commit()
        return sess.get(self.model, key)

    def delete(self, sess: Session, *, key: PrimaryKeySchemaType) -> ModelType | None:

        obj_to_delete = self.get(sess, key=key)
        if not obj_to_delete:
            return None

        sess.delete(obj_to_delete)
        sess.commit()
        sess.refresh(obj_to_delete)
        return obj_to_delete
