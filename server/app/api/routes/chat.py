from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat.service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = chat_service.chat(request.message)
    return ChatResponse(reply=reply)

@router.post("/chat/stream")
def stream_chat(request: ChatRequest):

    return StreamingResponse(
        chat_service.stream_chat(request.message),
        media_type="text/plain",
    )