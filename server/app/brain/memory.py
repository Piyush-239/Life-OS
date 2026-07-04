import json

from app.services.ai.llm.factory import get_llm


class MemoryBrain:

    def __init__(self):
        self.llm = get_llm()

    def extract(self, message: str):

        prompt = f"""
You are the Memory Brain of LIFE-OS.

Extract only long-term memories.

Remember only:
- Preferences
- Goals
- Projects
- Skills
- Relationships
- Habits

Never remember:
- Questions
- Greetings
- Temporary requests
- Small talk

Return ONLY JSON.

Example:

[
    {{
        "category":"preference",
        "content":"Favorite drink is coffee."
    }}
]

Message:

{message}
"""

        response = self.llm.chat(prompt)

        try:

            response = response.strip()

            if response.startswith("```"):
                response = response.split("\n", 1)[1]
                response = response.rsplit("```", 1)[0]

            return json.loads(response)

        except Exception:

            return []

    def retrieve(self, user_message: str, memories):

        memory_text = ""

        for memory in memories:

            memory_text += f"- [{memory.category}] {memory.content}\n"

        prompt = f"""
You are the Memory Retrieval Brain.

User asked:

{user_message}

Stored memories:

{memory_text}

Return ONLY the memories useful for answering.

Return JSON.

Example:

[
    "Favorite drink is coffee."
]
"""

        response = self.llm.chat(prompt)

        try:

            response = response.strip()

            if response.startswith("```"):
                response = response.split("\n", 1)[1]
                response = response.rsplit("```", 1)[0]

            return json.loads(response)

        except Exception:

            return []