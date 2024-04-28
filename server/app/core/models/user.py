from tortoise import fields, Model


class User(Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=64, unique=True)
    hashed_password = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)
