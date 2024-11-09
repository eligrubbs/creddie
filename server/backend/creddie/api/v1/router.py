from fastapi import APIRouter


from .endpoints import (
    categories,
    transactions
)

api_router = APIRouter()
api_router.include_router(categories.router, prefix="/category", tags=["category"])
api_router.include_router(transactions.router, prefix="/transaction", tags=["transaction"])
