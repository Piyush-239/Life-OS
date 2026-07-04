from app.database.models import Memory
from app.database.session import SessionLocal


class MemoryService:

    def save(self, memories, conversation_id):

        print("=== MEMORIES ===")
        print(memories)
        print(type(memories))

        session = SessionLocal()

        try:
            for memory in memories:
                print(memory)
                print(type(memory))

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

    def get_all(self):
        session = SessionLocal()

        try:
            return session.query(Memory).all()

        finally:
            session.close()