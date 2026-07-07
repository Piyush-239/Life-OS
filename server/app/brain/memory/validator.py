class MemoryValidator:

    def validate(self, candidates, existing_memories):

        approved = []

        existing = {
            (
                memory.category.lower(),
                memory.key.lower(),
                str(memory.value).lower(),
            )
            for memory in existing_memories
        }

        bad_values = {
            "",
            "unknown",
            "none",
            "null",
            "n/a",
            "not specified",
            "not mentioned",
            "withheld",
            "cannot determine",
        }

        for memory in candidates:

            if not isinstance(memory, dict):
                continue

            if "category" not in memory:
                continue

            if "key" not in memory:
                continue

            if "value" not in memory:
                continue

            value = memory["value"]

            if value is None:
                continue

            value = str(value).strip()

            if value.lower() in bad_values:
                continue

            key = (
                memory["category"].lower(),
                memory["key"].lower(),
                value.lower(),
            )

            if key in existing:
                continue

            approved.append({
                "category": memory["category"],
                "key": memory["key"],
                "value": value,
            })

        return approved