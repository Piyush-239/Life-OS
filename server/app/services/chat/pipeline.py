from app.services.ai.llm.factory import get_llm
from app.services.conversation.service import ConversationService
from app.services.memory.extractor import MemoryExtractor
from app.services.memory.retriever import MemoryRetriever
from app.services.memory.service import MemoryService
from app.services.prompt.builder import PromptBuilder


class ChatPipeline:

    def __init__(self):
        from app.brain.brain import Brain
        self.brain = Brain()

        self.conversation_service = ConversationService()

        self.memory_extractor = MemoryExtractor()
        self.memory_service = MemoryService()

        self.memory_retriever = MemoryRetriever()
        self.prompt_builder = PromptBuilder()

    def run(self, message: str):

        # Retrieve relevant memories
        memories = self.memory_retriever.retrieve(message)

        # Build prompt
        prompt = self.prompt_builder.build(
            user_message=message,
            memories=memories,
        )

        # Generate AI response
        reply = self.brain.chat.reply(prompt)

        # Save conversation
        conversation = self.conversation_service.save(
            user_message=message,
            assistant_message=reply,
        )

        # Extract memories from the new message
        new_memories = self.memory_extractor.extract(message)

        # Save them
        self.memory_service.save(
            memories=new_memories,
            conversation_id=conversation.id,
        )

        return reply