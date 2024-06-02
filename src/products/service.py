from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import Product
from sqlalchemy import select
from sqlalchemy.engine import Result
from src.products.schemas import ProductCreate


async def get_products(session: AsyncSession) -> list[Product]:
    query = select(Product).order_by(Product.id)
    result: Result = await session.execute(query)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(
    session: AsyncSession, product_in: ProductCreate
) -> Product | None:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh()
    return product
