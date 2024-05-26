from src.users.schemas import CreateUserORM


def create_user(user_in: CreateUserORM):
    user = user_in.model_dump()
    return {"success": True, "user": user}
