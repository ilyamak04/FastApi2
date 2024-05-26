from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr
from typing import Annotated


class CreateUserORM(BaseModel):
    email: EmailStr
    username: Annotated[str, MaxLen(20), MinLen(3)]
