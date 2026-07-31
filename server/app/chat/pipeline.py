from app.chat.chat import ChatBrain
from app.services.conversation.service import ConversationService
from app.services.prompt.builder import PromptBuilder


class ChatPipeline:

    def __init__(self):
        self.chat_brain = ChatBrain()
        self.conversation_service = ConversationService()
        self.prompt_builder = PromptBuilder()

    def run(self, message: str, memories=None) -> str:
        prompt = self.prompt_builder.build(
            user_message=message,
            memories=memories or [],
        )
        print("[PROMPT] built")

        reply = self.chat_brain.reply(prompt)

        self.conversation_service.save(
            user_message=message,
            assistant_message=reply,
        )

        return reply
