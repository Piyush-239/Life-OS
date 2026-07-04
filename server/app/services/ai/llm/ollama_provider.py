from ollama import Client

from app.core.settings import get_settings
from app.services.ai.llm.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    def __init__(self):
        settings = get_settings()

        self.client = Client(host=settings.ollama_host)
        self.model = settings.llm_model

    def chat(self, prompt: str):
        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]

    def stream_chat(self, message: str):
        stream = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            stream=True,
        )

        for chunk in stream:
            content = chunk["message"]["content"]

            if content:
                yield content