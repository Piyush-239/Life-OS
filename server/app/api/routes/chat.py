from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat.service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = chat_service.chat(request.message)
    return ChatResponse(reply=reply)