from app.core.models.user import User
from app.utils.exceptions import BadRequestError
from app.utils.password import get_password_hash


async def create_user(username: str, password: str):
    user = await User.get_or_none(username=username)
    if user:
        raise BadRequestError(detail=f"User({username}) already exists")
    return await User.create(username=username, hashed_password=get_password_hash(password))


async def get_gpt_user():
    gpt_user = await User.get_or_none(type=User.Type.GPT)
    if gpt_user:
        return gpt_user
    return await User.create(username='gpt', hashed_password=get_password_hash('gpt'), type=User.Type.GPT)
