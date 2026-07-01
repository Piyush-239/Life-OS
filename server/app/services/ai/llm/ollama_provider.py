from ollama import Client

from app.core.settings import get_settings
from app.services.ai.llm.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    def __init__(self):
        settings = get_settings()

        self.client = Client(host=settings.ollama_host)
        self.model = settings.llm_model

    def chat(self, message: str) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response["message"]["content"]