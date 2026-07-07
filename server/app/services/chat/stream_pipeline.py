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

        # Load all memories
        all_memories = self.memory_service.get_all()
        print("\n===== ALL MEMORIES FROM DB =====")

        for memory in all_memories:
            print(
                memory.category,
                memory.key,
                memory.value,
            )

        # Retrieve only relevant memories
        relevant_memories = all_memories

        print("\n===== RETRIEVED MEMORIES =====")
        for memory in relevant_memories:
            print(
                f"[{memory.category}] "
                f"{memory.key} = {memory.value}"
            )

        print("\nBuilding prompt with:")
        print(len(all_memories))

        for m in all_memories:
            print(m.category, m.key, m.value)
        

        # Build prompt
        prompt = self.prompt_builder.build(
            user_message=message,
            memories=relevant_memories,
        )

        full_reply = ""

        # Stream AI reply
        for chunk in self.brain.chat.stream_reply(prompt):
            full_reply += chunk
            yield chunk

        # Save conversation
        conversation = self.conversation_service.save(
            user_message=message,
            assistant_message=full_reply,
        )

        # Extract candidate memories
        candidates = self.brain.memory.extract(
            message,
        )

        print("\n===== Candidate Memories =====")
        print(candidates)

        # Validate candidates
        approved = self.brain.memory_validator.validate(
            candidates,
            all_memories,
        )

        print("\n===== Approved Memories =====")
        print(approved)

        # Save approved memories
        if approved:
            self.memory_service.save(
                approved,
                conversation.id,
            )