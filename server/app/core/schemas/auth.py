from fastapi import Form

from server.app.core.schemas.base import ChatbotModel


class UserCredentialForm(ChatbotModel):
    username: str
    password: str

    @classmethod
    def as_form(
            cls,
            username: str = Form(...),
            password: str = Form(...)
    ):
        return cls(username=username, password=password)


class TokenPayload(ChatbotModel):
    sub: str


class TokenOut(ChatbotModel):
    access_token: str
    token_type: str


class UserOut(ChatbotModel):
    id: int
    username: str


class LoginOut(ChatbotModel):
    user: UserOut
    token: TokenOut
