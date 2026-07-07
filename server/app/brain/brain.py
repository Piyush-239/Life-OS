from app.brain.chat import ChatBrain
from app.brain.memory import (
    MemoryExtractor,
    MemoryValidator,
    MemoryRetriever,
)


class Brain:

    def __init__(self):
        self.chat = ChatBrain()

        self.memory = MemoryExtractor()

        self.memory_validator = MemoryValidator()

        self.memory_retriever = MemoryRetriever()