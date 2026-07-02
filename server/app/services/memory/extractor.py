import json

from app.services.ai.llm.factory import get_llm


class MemoryExtractor:
    def __init__(self):
        self.llm = get_llm()

    def extract(self, message: str):
        prompt = f"""
Extract only long-term memories from this message.

Return ONLY valid JSON.

Format:
[
  {{
    "category": "goal",
    "content": "Build LIFE-OS"
  }}
]

If nothing is worth remembering, return:
[]

Message:
{message}
"""

        response = self.llm.chat(prompt)

        try:
            return json.loads(response)
        except Exception:
            return []