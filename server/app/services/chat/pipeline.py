from app.services.ai.llm.factory import get_llm
from app.services.conversation.service import ConversationService
from app.services.memory.extractor import MemoryExtractor
from app.services.memory.service import MemoryService


class ChatPipeline:

    def __init__(self):
        self.llm = get_llm()
        self.conversation_service = ConversationService()
        self.memory_extractor = MemoryExtractor()
        self.memory_service = MemoryService()

    def run(self, message: str):

        reply = self.llm.chat(message)

        conversation = self.conversation_service.save(
            user_message=message,
            assistant_message=reply,
        )

        memories = self.memory_extractor.extract(message)

        self.memory_service.save(
            memories,
            conversation.id,
        )

        return reply