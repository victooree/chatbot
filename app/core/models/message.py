from tortoise import Model, fields


class Message(Model):
    id = fields.BigIntField(pk=True)
    chat_room = fields.ForeignKeyField('models.ChatRoom', related_name='chat_room', index=True)
    sender = fields.ForeignKeyField('models.User', related_name='sender')
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "chat_rooms"
        index = [
            "chat_room_id",
        ]
