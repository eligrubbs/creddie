from fastapi import APIRouter, status, HTTPException

from ....schemas.transaction_schema import CreateTransaction, ReadTransaction, UpdateTransaction
from ....schemas.types import UUIDType
from ....crud import transactions, categories
from ....api.deps import SessDep

router = APIRouter()


@router.post("/", response_model=ReadTransaction, status_code=status.HTTP_201_CREATED)
async def create_transaction(create_info: CreateTransaction, sess: SessDep):
    """Create a Transaction."""
    if not categories.get(sess, key=create_info.category_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {create_info.category_id} not found.")

    created_obj = transactions.create(sess, obj_in=create_info)

    return created_obj


@router.get("/", response_model=ReadTransaction, status_code=status.HTTP_200_OK)
async def get_transaction_by_id(id: UUIDType, sess: SessDep):
    """Get a Transaction by it's ID."""
    got_obj = transactions.get(sess, key=id)

    if not got_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaction with id {id} not found")

    return got_obj


@router.put("/", response_model=ReadTransaction, status_code=status.HTTP_200_OK)
async def update_transaction(id: UUIDType, data: UpdateTransaction,sess: SessDep):
    """Update a Transaction."""

    upd_obj = transactions.update(sess, key=id, obj_in=data)

    if not upd_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaction with id {id} not found")

    return upd_obj


@router.delete("/", response_model=ReadTransaction, status_code=status.HTTP_202_ACCEPTED)
async def delete_transaction(id: UUIDType, sess: SessDep):
    """Delete a Transaction."""

    del_obj = transactions.delete(sess, key=id)

    if not del_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaction with id {id} not found")

    return del_obj

