from tortoise import Model, fields


class ChatRoom(Model):
    id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='users', db_constraint=False, index=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
