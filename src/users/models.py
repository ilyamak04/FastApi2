from src.models import Base
from sqlalchemy.orm import Mapped


class Product(Base):
    __tablename__ = "product"

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
