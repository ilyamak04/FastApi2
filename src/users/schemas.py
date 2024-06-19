from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Annotated


class CreateUserORM(BaseModel):
    email: EmailStr
    username: Annotated[str, MaxLen(20), MinLen(3)]


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True
