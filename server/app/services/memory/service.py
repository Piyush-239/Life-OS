from app.database.models import Memory
from app.database.session import SessionLocal


class MemoryService:
    def save(self, memories, conversation_id):
        session = SessionLocal()

        try:
            for memory in memories:
                session.add(
                    Memory(
                        category=memory["category"],
                        content=memory["content"],
                        source_conversation_id=conversation_id,
                    )
                )

            session.commit()

        finally:
            session.close()