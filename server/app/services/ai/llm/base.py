from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def chat(self, message: str) -> str:
        """Return a complete response."""
        pass

    @abstractmethod
    def stream_chat(self, message: str):
        """Yield response chunks."""
        pass