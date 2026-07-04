import re

from sqlalchemy import select

from app.database.models import Memory
from app.database.session import SessionLocal


class MemoryRetriever:

    STOP_WORDS = {
        "what", "who", "where", "when", "why", "how",
        "is", "are", "was", "were",
        "the", "a", "an",
        "my", "me", "i",
        "do", "does", "did",
        "tell", "about"
    }

    def retrieve(self, message: str):

        session = SessionLocal()

        try:

            # remove punctuation
            text = re.sub(r"[^\w\s]", "", message.lower())

            keywords = [
                word
                for word in text.split()
                if word not in self.STOP_WORDS and len(word) > 2
            ]

            memories = session.scalars(
                select(Memory)
            ).all()

            relevant = []

            for memory in memories:

                content = memory.content.lower()

                score = 0

                for word in keywords:
                    if word in content:
                        score += 1

                if score > 0:
                    relevant.append((score, memory))

            relevant.sort(reverse=True, key=lambda x: x[0])

            return [memory for _, memory in relevant[:5]]

        finally:
            session.close()