from fastapi import APIRouter, HTTPException, status
from src.products import service
from src.products.schemas import Product, ProductCreate

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(session):
    return await service.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(session, product_in: ProductCreate):
    return await service.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(product_id: int, session):
    product = await service.get_product(product_id=product_id, session=session)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"product {product_id} not found",
    )
