from fastapi import APIRouter, Depends

from app.core.models import User
from app.core.schemas.auth import UserOut
from app.services.dependencies import get_user

router = APIRouter(tags=['users'])


@router.get('/users/me', response_model=UserOut)
async def get_system_user_me(user: User = Depends(get_user)):
    return user
