from app.chat import ChatBrain
from app.memory import (
    ImportanceScorer,
    MemoryExtractor,
    MemoryValidator,
    MemoryRetriever,
)
from app.planner import ExecutivePlanner


class Brain:

    def __init__(self):

        self.chat = ChatBrain()

        self.memory = MemoryExtractor()

        self.memory_validator = MemoryValidator()

        self.memory_retriever = MemoryRetriever()

        self.importance = ImportanceScorer()

        self.planner = ExecutivePlanner()