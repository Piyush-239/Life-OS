from app.chat.chat import ChatBrain
from app.services.conversation.service import ConversationService
from app.services.prompt.builder import PromptBuilder


class StreamingChatPipeline:

    def __init__(self):
        self.chat_brain = ChatBrain()
        self.conversation_service = ConversationService()
        self.prompt_builder = PromptBuilder()

    def run(self, message: str, memories=None):
        prompt = self.prompt_builder.build(
            user_message=message,
            memories=memories or [],
        )
        print("[PROMPT] built")

        full_reply = ""

        for chunk in self.chat_brain.stream_reply(prompt):
            full_reply += chunk
            yield chunk

        self.conversation_service.save(
            user_message=message,
            assistant_message=full_reply,
        )
