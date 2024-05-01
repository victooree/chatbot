from fastapi import APIRouter, Depends

from app.core.models.user import User
from app.core.schemas.auth import TokenPayload, TokenOut, UserCredentialForm, LoginOut, \
    UserOut
from app.services.users import create_user
from app.utils.exceptions import UnauthorizedError
from app.utils.jwt import create_jwt_token
from app.utils.password import verify_password

router = APIRouter(tags=['auth'])


@router.post('/auth/sign-up', response_model=UserOut)
async def sign_up(sign_up_form: UserCredentialForm = Depends(UserCredentialForm.as_form)):
    user = await create_user(sign_up_form.username, sign_up_form.password)
    return user


@router.post("/auth/login", response_model=LoginOut)
async def login(form_data: UserCredentialForm = Depends(UserCredentialForm.as_form)):
    user = await User.get_or_none(username=form_data.username)
    if not user:
        raise UnauthorizedError(detail="Incorrect username")
    if not verify_password(form_data.password, user.hashed_password):
        raise UnauthorizedError(detail="Incorrect password")

    payload = TokenPayload(sub=user.username)
    token = create_jwt_token(payload.model_dump())
    return LoginOut(user=user, token=TokenOut(access_token=token, token_type="bearer"))
