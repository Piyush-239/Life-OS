from app.database.models import Memory
from app.database.session import SessionLocal
from app.vector.indexer import MemoryIndexer


class MemoryService:

    def __init__(self):
        self.indexer = MemoryIndexer()

    def save(self, memories, conversation_id):

        db = SessionLocal()

        try:

            updated_rows = []

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

                    updated_rows.append(existing)

                else:

                    memory_row = Memory(
                        category=memory["category"],
                        key=memory["key"],
                        value=memory["value"],
                        source_conversation_id=conversation_id,
                    )

                    db.add(memory_row)
                    updated_rows.append(memory_row)

            db.commit()

            # Index every inserted/updated memory
            for memory in updated_rows:
                print("INDEXING:", memory.category, memory.key, memory.value)
                self.indexer.add(memory)

        finally:
            db.close()

    def get_all(self):

        db = SessionLocal()

        try:
            return db.query(Memory).all()

        finally:
            db.close()