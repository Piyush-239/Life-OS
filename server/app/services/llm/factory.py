from app.services.llm.ollama_provider import OllamaProvider


def get_llm():
    return OllamaProvider()