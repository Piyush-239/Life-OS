from app.database.models import Memory
from app.database.session import SessionLocal


class MemoryService:

    def save(self, memories, conversation_id):

        db = SessionLocal()

        try:

            for memory in memories:

                existing = (
                    db.query(Memory)
                    .filter(
                        Memory.category == memory["category"],
                        Memory.key == memory["key"],
                    )
                    .first()
                )

                if existing:

                    existing.value = memory["value"]
                    existing.source_conversation_id = conversation_id

                else:

                    db.add(
                        Memory(
                            category=memory["category"],
                            key=memory["key"],
                            value=memory["value"],
                            source_conversation_id=conversation_id,
                        )
                    )

            db.commit()

        finally:
            db.close()

    def get_all(self):

        db = SessionLocal()

        try:
            return db.query(Memory).all()

        finally:
            db.close()