from app.services.ai.llm.factory import get_llm


class ChatService:
    def __init__(self):
        self.llm = get_llm()

    def chat(self, message: str) -> str:
        """
        Main chat pipeline.

        Future steps:
        1. Retrieve memories
        2. Inject system prompt
        3. Call planner if needed
        4. Send to LLM
        5. Save conversation
        6. Return response
        """

        return self.llm.chat(message)