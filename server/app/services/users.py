from server.app.core.models.user import User
from server.app.utils.exceptions import BadRequestError
from server.app.utils.password import get_password_hash


async def create_user(username: str, password: str):
    user = await User.get_or_none(username=username)
    if user:
        raise BadRequestError(detail=f"User({username}) already exists")
    return await User.create(username=username, hashed_password=get_password_hash(password))
