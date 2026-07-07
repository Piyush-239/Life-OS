import json

from app.services.ai.llm.factory import get_llm


class MemoryExtractor:

    def __init__(self):
        self.llm = get_llm()

    def extract(self, message: str):

        prompt = f"""
You are the Memory Extraction Engine.

Extract ONLY permanent facts from the user's message.

Return JSON only.

Each memory MUST have:

- category
- key
- value

Categories:

- personal
- preference
- project
- goal
- skill
- relationship
- habit

Examples

User:
My name is Piyush.

Output:

[
    {{
        "category":"personal",
        "key":"name",
        "value":"Piyush"
    }}
]

--------------------

User:
My favorite drink is coffee.

Output:

[
    {{
        "category":"preference",
        "key":"favorite_drink",
        "value":"coffee"
    }}
]

--------------------

User:
I am building LIFE-OS.

Output:

[
    {{
        "category":"project",
        "key":"current_project",
        "value":"LIFE-OS"
    }}
]

--------------------

Rules

Do NOT invent facts.

Do NOT summarize.

Do NOT explain.

Return ONLY JSON.

User message:

{message}
"""

        response = self.llm.chat(prompt)

        print("\n========== RAW LLM ==========")
        print(response)
        print("=============================\n")

        try:

            response = response.strip()

            if response.startswith("```"):
                response = response.split("\n", 1)[1]
                response = response.rsplit("```", 1)[0]

            memories = json.loads(response)

            if isinstance(memories, dict):
                memories = [memories]

            return memories

        except Exception as e:

            print("JSON ERROR:", e)
            return []