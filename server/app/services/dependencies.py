from typing import Optional

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from jose import JWTError

from server.app.core.models import User
from server.app.core.schemas.auth import TokenPayload
from server.app.utils.exceptions import UnauthorizedError, CredentialsError
from server.app.utils.jwt import auth_scheme, decode_jwt_token


async def verify_auth(bearer) -> TokenPayload:
    if not isinstance(bearer, HTTPAuthorizationCredentials):
        raise CredentialsError('Not authenticated')
    try:
        payload = decode_jwt_token(bearer.credentials)
        return TokenPayload(**payload)
    except JWTError as e:
        raise UnauthorizedError('JWT Error. Invalid token. ' + str(e))


async def get_user(bearer: Optional[HTTPAuthorizationCredentials] = Depends(auth_scheme)) -> User:
    payload = await verify_auth(bearer)
    return await User.get(username=payload.sub)
