from fastapi import APIRouter, Depends

from server.app.core.models import User
from server.app.core.schemas.messages import MessageListOut, MessageOut, MessageIn
from server.app.services.dependencies import get_user
from server.app.services import chat

router = APIRouter(tags=['chats'])


@router.get('/chats', response_model=MessageListOut)
async def get_chats(user: User = Depends(get_user)):
    return await chat.get_messages_records_of_chat_room(user)


@router.post('/chats', response_model=MessageOut)
async def get_user_answer_from_chat_client(message_in: MessageIn,
                                           user: User = Depends(get_user)):
    return await chat.get_new_answer_from_chat_client(user, message_in.content)