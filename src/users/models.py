from src.models import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, Text, mapped_column, relationship, String
from src.users.mixins import UserRelationMixin


class Product(Base):

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]


class Post(UserRelationMixin, Base):
    _user_id_nullable = False
    _user_id_unique = False
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        default_factory="",
    )


class User(Base):

    username: Mapped[str] = mapped_column(String(32), unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]
