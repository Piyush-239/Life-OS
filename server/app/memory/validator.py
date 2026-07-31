from app.memory.utils import normalize_key


class MemoryValidator:

    def validate(self, candidates, existing_memories):

        approved = []

        # Map existing memories by normalized_key (ignoring category) to value
        existing_keys = {
            normalize_key(memory.key): str(memory.value).lower().strip()
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

            if (
                "category" not in memory
                or "key" not in memory
                or "value" not in memory
            ):
                continue

            value = memory["value"]

            if value is None:
                continue

            value = str(value).strip()

            if value.lower() in bad_values:
                continue

            norm_k = normalize_key(memory["key"])

            # If the normalized key already exists anywhere in the database
            if norm_k in existing_keys:
                # If the value is exactly the same, reject as duplicate
                if existing_keys[norm_k] == value.lower():
                    continue
                # If value is different, it's a valid update -> approved!

            approved.append({
                "category": memory["category"],
                "key": memory["key"],
                "value": value,
            })

        return approved
