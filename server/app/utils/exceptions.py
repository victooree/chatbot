from fastapi import HTTPException
from starlette import status


class BaseError(HTTPException):
    def __init__(self, status_code, title, detail, headers=None):
        self.title = title
        super().__init__(status_code=status_code,
                         detail=detail,
                         headers=headers)

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(title={self.title!r}, status_code={self.status_code!r}, detail={self.detail!r})"


class UnauthorizedError(BaseError):
    def __init__(self, detail):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         title='unauthorized',
                         detail=detail)


class BadRequestError(BaseError):
    def __init__(self, detail):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST,
                         title='Bad Request',
                         detail=detail)


class UnauthorizedError(BaseError):
    def __init__(self, detail):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         title='unauthorized',
                         detail=detail)


class CredentialsError(BaseError):
    def __init__(self, detail):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         title='Credentials Error',
                         detail=detail,
                         headers={"WWW-Authenticate": "Bearer"})