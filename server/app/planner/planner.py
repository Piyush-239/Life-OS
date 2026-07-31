import json
import re
from pathlib import Path
import ollama

from app.core.settings import get_settings


class ExecutivePlanner:

    def __init__(self):
        settings = get_settings()
        self.model = "qwen2.5:0.5b"
        self.host = settings.ollama_host

        # Load the prompt relative to the planner directory
        prompt_path = Path(__file__).parent / "planner_prompt.txt"
        self.system = prompt_path.read_text(encoding="utf-8")

    def plan(self, user_message: str):
        cleaned = user_message.lower().strip().rstrip("?")

        # 1. Deterministic Rule-based Overrides for absolute certainty
        if cleaned in ["hello", "hello!", "hi", "hi!", "hey"]:
            return {
                "intent": "chat",
                "needs_memory": False,
                "needs_chat": True,
                "needs_tools": False,
                "needs_web": False,
                "confidence": 1.0,
            }

        if "joke" in cleaned:
            return {
                "intent": "chat",
                "needs_memory": False,
                "needs_chat": True,
                "needs_tools": False,
                "needs_web": False,
                "confidence": 1.0,
            }

        if cleaned in [
            "do you know who i am",
            "do you know who i am?",
            "do you know me",
            "do you know me?",
        ]:
            return {
                "intent": "chat",
                "needs_memory": False,
                "needs_chat": True,
                "needs_tools": False,
                "needs_web": False,
                "confidence": 1.0,
            }

        if cleaned in [
            "tell me about me",
            "tell me about me.",
            "what do you know about me",
            "what do you know about me?",
            "tell me everything you know about me",
        ]:
            return {
                "intent": "memory_query",
                "needs_memory": True,
                "needs_chat": True,
                "needs_tools": False,
                "needs_web": False,
                "confidence": 1.0,
            }

        if cleaned.startswith("print ") and "pdf" in cleaned:
            return {
                "intent": "tool",
                "needs_memory": False,
                "needs_chat": False,
                "needs_tools": True,
                "needs_web": False,
                "confidence": 1.0,
            }

        # Calculator check
        if re.match(r"^[\d\s\+\-\*\/\(\)\.]+$", cleaned):
            return {
                "intent": "calculator",
                "needs_memory": False,
                "needs_chat": False,
                "needs_tools": True,
                "needs_web": False,
                "confidence": 1.0,
            }

        # Web search check
        if (
            "prime minister" in cleaned
            or "president" in cleaned
            or "weather" in cleaned
            or "news" in cleaned
            or "who won" in cleaned
            or "who is" in cleaned
        ):
            return {
                "intent": "web_search",
                "needs_memory": False,
                "needs_chat": True,
                "needs_tools": False,
                "needs_web": True,
                "confidence": 1.0,
            }

        # Memory store check for statements or corrections
        if (
            cleaned.startswith("no ")
            or cleaned.startswith("no,")
            or cleaned.startswith("actually")
            or cleaned.startswith("correction")
            or cleaned.startswith("update")
        ):
            if "my" in cleaned or "is" in cleaned:
                return {
                    "intent": "memory_store",
                    "needs_memory": True,
                    "needs_chat": False,
                    "needs_tools": False,
                    "needs_web": False,
                    "confidence": 1.0,
                }

        if (
            (
                cleaned.startswith("my ")
                or cleaned.startswith("remember ")
                or cleaned.startswith("store ")
            )
            and ("is" in cleaned or "name" in cleaned)
            and not cleaned.startswith("what")
        ):
            return {
                "intent": "memory_store",
                "needs_memory": True,
                "needs_chat": False,
                "needs_tools": False,
                "needs_web": False,
                "confidence": 1.0,
            }

        if (
            cleaned.startswith("what is my")
            or cleaned.startswith("what's my")
            or cleaned.startswith("what do you remember")
        ):
            return {
                "intent": "memory_query",
                "needs_memory": True,
                "needs_chat": True,
                "needs_tools": False,
                "needs_web": False,
                "confidence": 1.0,
            }

        # 2. LLM Call Fallback
        client = ollama.Client(host=self.host)
        response = client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.system,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            stream=False,
        )

        text = response["message"]["content"]

        try:
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )
            plan = json.loads(text)
        except Exception as e:
            print(f"PLAN PARSE ERROR: {e}")
            return {
                "intent": "chat",
                "needs_memory": False,
                "needs_chat": True,
                "needs_tools": False,
                "needs_web": False,
                "confidence": 0.5,
            }

        VALID_INTENTS = {
            "chat",
            "memory_store",
            "memory_query",
            "calculator",
            "web_search",
            "tool",
            "vision",
            "document",
            "automation",
            "planning",
            "clarification",
            "coding",
        }

        intent = plan.get("intent", "chat").strip().lower()
        if intent not in VALID_INTENTS:
            intent = "chat"

        return {
            "intent": intent,
            "needs_memory": bool(plan.get("needs_memory", False)),
            "needs_chat": bool(
                plan.get(
                    "needs_chat", True if intent == "chat" else False
                )
            ),
            "needs_tools": bool(plan.get("needs_tools", False)),
            "needs_web": bool(plan.get("needs_web", False)),
            "confidence": float(plan.get("confidence", 1.0)),
        }
