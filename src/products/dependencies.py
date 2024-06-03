from fastapi import HTTPException, status, Path, Depends
from src.products import service
from src.database import db_helper
from src.users.models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated


async def product_by_id(
    product_id: Annotated[int, Path()],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    product = await service.get_product(product_id=product_id, session=session)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"product {product_id} not found",
    )
