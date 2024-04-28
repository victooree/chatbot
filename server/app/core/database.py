from tortoise.contrib.fastapi import register_tortoise

from server.app.core.settings import get_settings


def get_config(database_uri):
    return {
        'connections': {
            'models': database_uri,
            'ro_models': database_uri
        },
        'apps': {
            'models': {
                'models': ['server.app.core.models'],
                'default_connection': 'models'
            }
        },
        'use_tz': True,
        "timezone": "UTC",
    }


def init_orm(app):
    settings = get_settings()
    register_tortoise(
        app,
        config=get_config(settings.DATABASE_URL),
        generate_schemas=settings.GENERATE_SCHEMAS,
        add_exception_handlers=False)
