from pydantic import BaseModel


class CommonError(BaseModel):
    code: str
    title: str
    detail: str
