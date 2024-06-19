from src.models import Base
from sqlalchemy import (
    ForeignKey,
    UniqueConstraint,
    Table,
    Column,
    String,
    func,
    Integer,
)
from sqlalchemy.orm import Mapped, Text, mapped_column, relationship, String
from src.users.mixins import UserRelationMixin
from datetime import datetime


class Product(Base):

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]

    oders: Mapped[list["Order"]] = relationship(
        back_populates="products",
        secondary="order_product_association_table",
    )

    orders_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="product",
    )


class Order(Base):

    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
    products: Mapped[list["Product"]] = relationship(
        back_populates="orders",
        secondary="order_product_association_table",
    )

    products_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="order",
    )


# order_product_association_table = Table(
#     "order_product_asociation",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("order_id", ForeignKey("order.id"), nullable=False),
#     Column("product_id", ForeignKey("product.id"), nullable=False),
#     UniqueConstraint("order_id", "product_id", name="idx_inique_order_product"),
# )


class OrderProductAssociation(Base):
    __tablename__ = "order_product_association"
    __table_args__ = (
        UniqueConstraint(
            "order_id",
            "product_id",
            name="idx_inique_order_product",
        ),
    )

    id: Mapped[int] = (mapped_column(primary_key=True),)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    count: Mapped[int] = mapped_column(default=1, server_default="1")
    unit_price: Mapped[int] = mapped_column(default=0, server_default="0")

    order: Mapped["Order"] = relationship(back_populates="products_details")

    product: Mapped["Product"] = relationship(back_populates="orders_details")
