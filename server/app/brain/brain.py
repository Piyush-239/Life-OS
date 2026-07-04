from app.brain.chat import ChatBrain
from app.brain.memory import MemoryBrain


class Brain:

    def __init__(self):
        self.chat = ChatBrain()
        self.memory = MemoryBrain()