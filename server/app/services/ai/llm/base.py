from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """Abstract base class for all LLM providers."""

    @abstractmethod
    def chat(self, message: str) -> str:
        """Send a message to the language model."""
        pass