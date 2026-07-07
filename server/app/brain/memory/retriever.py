class MemoryRetriever:

    def retrieve(self, message, memories):

        message = message.lower()

        results = []

        for memory in memories:

            text = (
                f"{memory.category} "
                f"{memory.key} "
                f"{memory.value}"
            ).lower()

            if any(word in text for word in message.split()):
                results.append(memory)

        return results