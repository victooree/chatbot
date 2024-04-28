from openai import AsyncOpenAI

from server.app.core.settings import get_settings
from server.app.utils.exceptions import ExternalServiceError
from server.app.utils.singleton import Singleton


def get_system_message():
    return {'role': 'system',
            'content': '너는 엄청 친절하고 ~요 를 사용하는 한국인이야. '
                       '너는 한국 영화나 드라마를 엄청 많이 알고, '
                       '사람들이 원하는 장르나 테마에 따라 영화나 드라마를 추천해주고 간단히 설명해주는 역할을 하는 보조자야.'
                       '외국어로 물어봐도 한글로 답해주면 되고, 영화나 드라마의 추천 이외에 질문에 대해서는 잘 모른다고 답해도 돼.'}


class ChatClient(object, metaclass=Singleton):
    def __init__(self):
        self.open_api_key = get_settings().OPENAI_API_KEY
        self.client = AsyncOpenAI(
            api_key=self.open_api_key,
        )

    async def get_answer(self, context: list[dict], temperature=1):
        try:
            completion = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=context,
                temperature=temperature,
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise ExternalServiceError(f"ChatClient.get_answer failed: {e}")
