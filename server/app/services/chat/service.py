from app.services.chat.pipeline import ChatPipeline


class ChatService:

    def __init__(self):
        self.pipeline = ChatPipeline()

    def chat(self, message: str):

        return self.pipeline.run(message)