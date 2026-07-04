from app.brain.brain import Brain
from app.services.conversation.service import ConversationService
from app.services.memory.service import MemoryService
from app.services.prompt.builder import PromptBuilder


class ChatPipeline:

    def __init__(self):

        self.brain = Brain()

        self.conversation_service = ConversationService()

        self.memory_service = MemoryService()

        self.prompt_builder = PromptBuilder()

    def run(self, message: str):

        # Load all memories
        all_memories = self.memory_service.get_all()

        # AI chooses relevant memories
        relevant_memories = self.brain.memory.retrieve(
            message,
            all_memories,
        )

        # Build prompt
        prompt = self.prompt_builder.build(
            user_message=message,
            memories=relevant_memories,
        )

        # Generate reply
        reply = self.brain.chat.reply(prompt)

        # Save conversation
        conversation = self.conversation_service.save(
            user_message=message,
            assistant_message=reply,
        )

        # Extract new memories
        new_memories = self.brain.memory.extract(message)

        # Save new memories
        self.memory_service.save(
            memories=new_memories,
            conversation_id=conversation.id,
        )

        return reply