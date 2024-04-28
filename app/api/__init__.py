from fastapi import APIRouter
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from app.utils.errors import CommonError

from app.api import chat, user, auth

router = APIRouter(responses={HTTP_422_UNPROCESSABLE_ENTITY: {'model': CommonError}})


router.include_router(auth.router)
router.include_router(user.router)
router.include_router(chat.router)
