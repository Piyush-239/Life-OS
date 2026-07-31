from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.chat import ChatRequest, ChatResponse
from app.router.router import ExecutionRouter

router = APIRouter()
execution_router = ExecutionRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = execution_router.handle(request.message)
    return ChatResponse(reply=reply)


@router.post("/chat/stream")
def stream_chat(request: ChatRequest):
    return StreamingResponse(
        execution_router.handle_stream(request.message),
        media_type="text/plain",
    )