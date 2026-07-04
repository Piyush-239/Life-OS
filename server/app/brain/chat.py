from app.services.ai.llm.factory import get_llm


class ChatBrain:

    def __init__(self):
        self.llm = get_llm()

    def reply(self, prompt: str):
        return self.llm.chat(prompt)

    def stream_reply(self, prompt: str):
        return self.llm.chat_stream(prompt)