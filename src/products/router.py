from fastapi import APIRouter, HTTPException, status, Depends
from src.products import service
from src.products.schemas import (
    Product,
    ProductCreate,
    ProductUpdate,
    ProductUpdatePartial,
)
from src.database import db_helper
from src.products.dependencies import product_by_id
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Products"], prefix="/products")


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await service.get_products(session=session)


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await service.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(product: Product = Depends(product_by_id)):
    return product


@router.put("/{product_id}/", response_model=Product)
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await service.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch("/{product_id}/", response_model=Product)
async def partial_update_product(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await service.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await service.delete_product(
        session=session,
        product=product,
    )
