from app.services.chat.pipeline import ChatPipeline
from app.services.chat.stream_pipeline import StreamingChatPipeline


class ChatService:
    def __init__(self):
        self.pipeline = ChatPipeline()
        self.streaming_pipeline = StreamingChatPipeline()

    def chat(self, message: str):
        return self.pipeline.run(message)

    def stream_chat(self, message: str):
        return self.streaming_pipeline.run(message)