from fastapi import APIRouter

from app.services.llm.factory import get_llm

router = APIRouter()


@router.get("/chat")
def chat():
    llm = get_llm()

    reply = llm.chat("Hello")

    return {
        "reply": reply
    }