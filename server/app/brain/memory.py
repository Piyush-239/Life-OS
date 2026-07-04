import json

from app.services.ai.llm.factory import get_llm


class MemoryBrain:

    def __init__(self):

        self.llm = get_llm()