from app.brain.brain import Brain
from app.services.conversation.service import ConversationService
from app.services.memory.service import MemoryService
from app.services.prompt.builder import PromptBuilder


class StreamingChatPipeline:

    def __init__(self):
        self.brain = Brain()
        self.conversation_service = ConversationService()
        self.memory_service = MemoryService()
        self.prompt_builder = PromptBuilder()

    def run(self, message: str):

        # Retrieve all memories
        all_memories = self.memory_service.get_all()

        # AI selects relevant memories
        relevant_memories = self.brain.memory.retrieve(
            message,
            all_memories,
        )

        # Build prompt
        prompt = self.prompt_builder.build(
            user_message=message,
            memories=relevant_memories,
        )

        full_reply = ""

        # Stream AI response
        for chunk in self.brain.chat.stream_reply(prompt):
            full_reply += chunk
            yield chunk

        # Save conversation
        conversation = self.conversation_service.save(
            user_message=message,
            assistant_message=full_reply,
        )

        # Extract memories from this message
        new_memories = self.brain.memory.extract(message)

        # Save memories
        self.memory_service.save(
            memories=new_memories,
            conversation_id=conversation.id,
        )