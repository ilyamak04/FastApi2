from fastapi import APIRouter

from src.users.schemas import CreateUserORM
from src.users.service import create_user


user_router = APIRouter(prefix="/users")


@user_router.post("/")
def create_user_view(user: CreateUserORM):
    return create_user(user)
