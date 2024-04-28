from tortoise.transactions import in_transaction

from server.app.core.models import User
from server.app.core.models.chat_room import ChatRoom
from server.app.core.models.message import Message
from server.app.core.schemas.messages import MessageOut
from server.app.services.messages import get_messages_of_chat_room
from server.app.services.users import get_gpt_user
from server.app.utils.chat_client import get_system_message, ChatClient


async def get_chat_room_or_create(user: User):
    chat_room = await ChatRoom.get_or_none(user=user)
    if chat_room is None:
        chat_room = await ChatRoom.create(user=user)
    return chat_room


async def get_new_answer_from_chat_client(user: User, question: str) -> MessageOut:
    chat_room = await get_chat_room_or_create(user)
    message_records = await get_messages_of_chat_room(chat_room.id)
    context = build_context(message_records, question)
    answer = await ChatClient().get_answer(context)
    async with in_transaction("models") as conn:
        gpt = await get_gpt_user()
        question_message = await Message.create(chat_room=chat_room, content=question, sender=user)
        await question_message.save(using_db=conn)

        answer_message = await Message.create(chat_room=chat_room, content=answer, sender=gpt)
        await answer_message.save(using_db=conn)
        return MessageOut(id=answer_message.id,
                          message=answer_message.content,
                          sender_type=gpt.type,
                          created_at=answer_message.created_at)


# TODO: 아래 내용 테스트 코드로 작성
def build_context(message_records: list[Message], new_question: str):
    context = [get_system_message()]
    for message in message_records:
        context.append(
            {"role": "user" if message.sender.type == User.Type.BASIC else "assistant", "content": message.content})
    context.append({"role": "user", "content": new_question})
    return context
