from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int
    description: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
