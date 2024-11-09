from fastapi import APIRouter, status, HTTPException

from ....schemas.category_schema import CreateCategory, ReadCategory, UpdateCategory
from ....schemas.types import UUIDType
from ....crud import categories
from ....api.deps import SessDep


router = APIRouter()

@router.post("/", response_model=ReadCategory, status_code=status.HTTP_201_CREATED)
async def create_category(create_info: CreateCategory, sess: SessDep):
    """Create a Category."""
    if categories.get_by_name(sess, name=create_info.name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Category already exists with name {create_info.name}")

    created_obj = categories.create(sess, obj_in=create_info)

    return created_obj


@router.get("/", response_model=ReadCategory, status_code=status.HTTP_200_OK)
async def get_category_by_id(id: UUIDType, sess: SessDep):
    """Get a Category by it's ID."""
    got_obj = categories.get(sess, key=id)

    if not got_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {id} not found")

    return got_obj


@router.put("/", response_model=ReadCategory, status_code=status.HTTP_200_OK)
async def update_category(id: UUIDType, data: UpdateCategory,sess: SessDep):
    """Update a Category."""

    upd_obj = categories.update(sess, key=id, obj_in=data)

    if not upd_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {id} not found")

    return upd_obj


@router.delete("/", response_model=ReadCategory, status_code=status.HTTP_202_ACCEPTED)
async def delete_category(id: UUIDType, sess: SessDep):
    """Delete a Category."""

    del_obj = categories.delete(sess, key=id)

    if not del_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {id} not found")

    return del_obj


@router.get("/all", response_model=list[ReadCategory], status_code=status.HTTP_200_OK)
async def get_all_categories(sess: SessDep):
    """Get a Category by it's ID."""

    return categories.get_all(sess)
