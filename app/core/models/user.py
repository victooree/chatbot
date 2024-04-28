from enum import StrEnum

from tortoise import fields, Model


class User(Model):
    class Type(StrEnum):
        BASIC = 'BASIC'
        GPT = 'GPT'

    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=64, unique=True)
    hashed_password = fields.CharField(max_length=128)
    type = fields.CharEnumField(Type, max_length=16, default=Type.BASIC)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)
