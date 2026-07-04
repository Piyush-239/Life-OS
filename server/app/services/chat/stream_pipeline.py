from app.services.ai.llm.factory import get_llm
from app.services.conversation.service import ConversationService
from app.services.memory.extractor import MemoryExtractor
from app.services.memory.service import MemoryService


class StreamingChatPipeline:
    def __init__(self):
        self.llm = get_llm()
        self.conversation_service = ConversationService()
        self.memory_extractor = MemoryExtractor()
        self.memory_service = MemoryService()

    def run(self, message: str):
        full_reply = ""

        for chunk in self.llm.stream_chat(message):
            full_reply += chunk
            yield chunk

        conversation = self.conversation_service.save(
            user_message=message,
            assistant_message=full_reply,
        )

        memories = self.memory_extractor.extract(message)

        self.memory_service.save(
            memories=memories,
            conversation_id=conversation.id,
        )