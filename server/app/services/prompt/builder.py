from pathlib import Path

SYSTEM_PROMPT = Path(
    "app/services/prompt/system_prompt.txt"
).read_text(encoding="utf-8")


class PromptBuilder:

    def build(
        self,
        user_message: str,
        memories,
    ) -> str:

        prompt = SYSTEM_PROMPT

        prompt += "\n\n========== MEMORY DATABASE ==========\n"

        if memories:

            for memory in memories:

                prompt += (
                    f"[{memory.category.upper()}] "
                    f"{memory.key} = {memory.value}\n"
                )    

        else:
            prompt += "EMPTY\n"

        prompt += "=====================================\n"

        prompt += f"""

========== CURRENT USER MESSAGE ==========

{user_message}

==========================================

Assistant:
"""

        print("\n========== FINAL PROMPT ==========")
        print(prompt)
        print("==================================\n")

        return prompt