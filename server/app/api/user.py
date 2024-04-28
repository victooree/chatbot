from fastapi import APIRouter, Depends

from server.app.core.models import User
from server.app.core.schemas.auth import UserOut
from server.app.services.dependencies import get_user

router = APIRouter(tags=['users'])


@router.get('/users/me', response_model=UserOut)
async def get_system_user_me(user: User = Depends(get_user)):
    return user
