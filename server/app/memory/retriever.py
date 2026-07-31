class MemoryRetriever:

    def retrieve(self, message, memories):
        # Normalize query: lower-case and replace punctuation with spaces
        cleaned = message.lower()
        for char in "?.,!':_-/\\":
            cleaned = cleaned.replace(char, " ")

        # Extract words longer than 1 character to avoid matching noise (like 's')
        words = [
            w.strip()
            for w in cleaned.split()
            if len(w.strip()) > 1
        ]

        results = []

        for memory in memories:

            text = (
                f"{memory.category} "
                f"{memory.key} "
                f"{memory.value}"
            ).lower()

            if any(word in text for word in words):
                results.append(memory)

        return results
