from datetime import datetime

from server.app.core.models import User
from server.app.core.schemas.base import ChatbotModel


class MessageIn(ChatbotModel):
    content: str


class MessageOut(ChatbotModel):
    id: int
    message: str
    sender_type: User.Type
    created_at: datetime


class MessageListOut(ChatbotModel):
    messages: list[MessageOut]
