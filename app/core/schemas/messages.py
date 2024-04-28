from datetime import datetime

from app.core.models import User
from app.core.schemas.base import ChatbotModel


class MessageIn(ChatbotModel):
    content: str


class MessageOut(ChatbotModel):
    id: int
    content: str
    sender_type: User.Type
    created_at: datetime


class MessageListOut(ChatbotModel):
    messages: list[MessageOut]
