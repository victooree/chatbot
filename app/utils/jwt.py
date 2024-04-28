from datetime import timedelta, timezone, datetime

from fastapi.security import HTTPBearer
from jose import jwt

from app.core.settings import get_settings

auth_scheme = HTTPBearer(scheme_name='Bearer', auto_error=False)


def create_jwt_token(data: dict, expires_in: int = get_settings().LOGIN_TOKEN_EXPIRES_TTL):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
    to_encode['exp'] = expire
    return jwt.encode(to_encode, get_settings().LOGIN_SECRET_KEY, algorithm="HS256")


def decode_jwt_token(token: str):
    return jwt.decode(token, get_settings().LOGIN_SECRET_KEY, algorithms=["HS256"])
