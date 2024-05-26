from users.schemas import CreateUser


def create_user(user: CreateUser):
    new_user = user.model_dump()
    return {"success": True, "user": new_user}
