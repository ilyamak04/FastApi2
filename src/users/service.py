from src.users.schemas import CreateUserORM
from src.users.models import *
from src.database import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload


def create_user(user_in: CreateUserORM):
    user = user_in.model_dump()
    return {"success": True, "user": user}


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    query = select(User).where(User.username == username)
    result: Result = await session.execute(query)
    user: User | None = result.scalar_one_or_none()
    # user: User | None = await session.scalars(query)
    return user


async def show_users_with_profile(session: AsyncSession) -> list[User]:
    query = select(User).options(joinedload(User.profile)).order_by(User.id)
    # result: Result = await session.execute()
    # users = result.scalars()
    users = await session.scalars(query)
    return users


async def create_posts(
    session: AsyncSession,
    user_id: int,
    *posts_titles: str,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in posts_titles]
    session.add_all(posts)
    await session.commit()
    return posts


async def get_users_with_posts(session: AsyncSession):
    # query = select(User).options(joinedload(User.posts)).order_by(User.id)
    query = select(User).options(selectinload(User.posts)).order_by(User.id)
    result: Result = await session.execute(query)
    # users = result.unique.scalars()
    users = result.scalars()
    # users = await session.scalars(query)
    return users


async def get_porfile_with_users_and_users_with_posts(session: AsyncSession):
    query = (
        select(Profile)
        .join(Profile.user)
        .options(
            joinedload(Profile.user).selectinload(User.posts),
        )
        .where(User.username == "john")
        .order_by(Profile.id)
    )
    profiles = await session.scalars(query)
    return profiles


async def get_users_with_posts_and_profiles(
    session: AsyncSession,
):
    query = (
        select(User)
        .options(
            joinedload(User.profile),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    users = await session.scalars(query)
    return users
