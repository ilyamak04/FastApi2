from fastapi import APIRouter
from users.schemas import CreateUser
from users.service import create_user


router = APIRouter(prefix="/users")


@router.post("")
def create_user(user: CreateUser):
    return create_user(user)
