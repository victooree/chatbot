from fastapi import APIRouter
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from server.app.utils.errors import CommonError


from server.app.api import (auth, user)

router = APIRouter(responses={HTTP_422_UNPROCESSABLE_ENTITY: {'model': CommonError}})


router.include_router(auth.router)
router.include_router(user.router)
