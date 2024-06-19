from fastapi import APIrouter, Depends, HTTPException
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIrouter(prefix="/demo-auth", tags=["Demo Auth"])

security = HTTPBasic()


@router.get("/basic-auth/")
def demo_basic_auth(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {
        "message": "Hi",
        "username": credentials.username,
        "password": credentials.password,
    }


# def get_auth_user_username(
#     credentials: Annotated[HTTPBasicCredentials, Depends(security)],
# ) -> str:
#     unauthed_exc = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid username or password",
#         headers={"WWW-Authenticate": "Basic"},
#     )
#     correct_password = usernames_to_passwords.get(credentials.username)
#     if correct_password is None:
#         raise unauthed_exc

#     # secrets
#     if not secrets.compare_digest(
#         credentials.password.encode("utf-8"),
#         correct_password.encode("utf-8"),
#     ):
#         raise unauthed_exc

#     return credentials.username
