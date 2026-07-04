from pathlib import Path

SYSTEM_PROMPT = Path(
    "app/services/prompt/system_prompt.txt"
).read_text(encoding="utf-8")


class PromptBuilder:

    def build(
        self,
        user_message: str,
        memories: list[str],
    ) -> str:

        prompt = SYSTEM_PROMPT

        prompt += "\n\nRelevant memories:\n"

        if memories:
            for memory in memories:
                prompt += f"\n- {memory}"
        else:
            prompt += "\n(None)"

        prompt += f"\n\nCurrent user message:\n\n{user_message}"

        return prompt