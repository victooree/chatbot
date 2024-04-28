from typing import Optional, Literal, Union, List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='server/.env', extra='allow')

    GENERATE_SCHEMAS: bool = False
    PROJECT_NAME: str = 'chatbot-api'
    BACKEND_CORS_ORIGINS: List[Union[AnyHttpUrl, Literal['*']]]

    DATABASE_URL: Optional[Union[str, Literal['sqlite://:memory:']]]

    LOGIN_SECRET_KEY: str
    LOGIN_TOKEN_EXPIRES_TTL: int = 60 * 60 * 24  # 1 day
    OPENAI_API_KEY: str


_settings = None


def get_settings(new_settings=None):
    global _settings
    if _settings is None:
        if new_settings is None:
            _settings = Settings()
        else:
            _settings = new_settings

    return _settings
