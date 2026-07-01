from app.services.llm.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    def chat(self, message: str) -> str:
        return "Ollama provider is not implemented yet."