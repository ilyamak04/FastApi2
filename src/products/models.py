from src.models import Base
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, Text, mapped_column, relationship, String
from src.users.mixins import UserRelationMixin
from datetime import datetime


class Product(Base):

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]


class Order(Base):
    promocode: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
