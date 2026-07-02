from app.services.ai.llm.factory import get_llm
from app.services.conversation.service import ConversationService
from app.services.memory.extractor import MemoryExtractor
from app.services.memory.service import MemoryService


class ChatService:
    def __init__(self):
        self.llm = get_llm()
        self.conversation_service = ConversationService()
        self.memory_extractor = MemoryExtractor()
        self.memory_service = MemoryService()

    def chat(self, message: str) -> str:
        # Step 1: Generate AI response
        reply = self.llm.chat(message)

        # Step 2: Save conversation
        conversation = self.conversation_service.save(
            user_message=message,
            assistant_message=reply,
        )
        print("Conversation:", conversation)
        

        # Step 3: Extract memories from the user's message
        memories = self.memory_extractor.extract(message)

        # Step 4: Save extracted memories
        self.memory_service.save(
            memories=memories,
            conversation_id=conversation.id,
        )

        # Step 5: Return AI response
        return reply