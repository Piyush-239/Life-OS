class MemoryExtractor:

    def extract(self, message: str):

        text = message.lower()

        memories = []

        # Favorite things
        if "my favorite" in text:
            memories.append({
                "category": "preference",
                "content": message
            })

        # Projects
        if "i'm building" in text or "i am building" in text:
            memories.append({
                "category": "project",
                "content": message
            })

        # Goals
        if "i want to" in text:
            memories.append({
                "category": "goal",
                "content": message
            })

        # Learning
        if "i'm learning" in text or "i am learning" in text:
            memories.append({
                "category": "learning",
                "content": message
            })

        return memories