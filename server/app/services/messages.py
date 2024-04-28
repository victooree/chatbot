from server.app.core.models.message import Message


async def get_messages_of_chat_room(chat_room_id: int):
    return await Message.filter(chat_room_id=chat_room_id).order_by('created_at').prefetch_related('sender')
