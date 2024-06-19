from sqlalchemy.ext.asyncio import AsyncSession
from src.products.models import Product, Order, OrderProductAssociation
from sqlalchemy import select
from sqlalchemy.engine import Result
from src.products.schemas import ProductCreate, ProductUpdate, ProductUpdatePartial
from sqlalchemy.orm import joinedload, selectinload


async def get_products(session: AsyncSession) -> list[Product]:
    query = select(Product).order_by(Product.id)
    result: Result = await session.execute(query)
    products = result.scalars().all()
    return products


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


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    await session.commit()


async def get_order_with_with_product_assoc(session: AsyncSession) -> list[Order]:
    query = (
        select(Order)
        .options(
            selectinload(Order.products_details).joinedload(
                OrderProductAssociation.product
            ),
        )
        .order_by(Order.id)
    )
    orders = await session.scalars(query)

    return list(orders)
