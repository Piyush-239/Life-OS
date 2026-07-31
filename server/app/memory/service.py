from app.database.models import Memory
from app.database.session import SessionLocal
from app.vector.indexer import MemoryIndexer
from app.memory.utils import normalize_key


class MemoryService:

    def __init__(self):
        self.indexer = MemoryIndexer()

    def save(self, memories, conversation_id):

        db = SessionLocal()

        try:

            updated_rows = []

            # Retrieve all existing rows for normalized matching
            existing_memories = db.query(Memory).all()

            for memory in memories:

                normalized_target = normalize_key(memory["key"])

                # Find matches comparing normalized key only (ignoring category)
                existing = None
                for row in existing_memories:
                    if normalize_key(row.key) == normalized_target:
                        existing = row
                        break

                if existing:
                    # Update value, importance, and match category/key name to latest extraction
                    existing.value = memory["value"]
                    existing.importance = memory["importance"]
                    existing.category = memory["category"]
                    existing.key = memory["key"]
                    existing.source_conversation_id = conversation_id
                    updated_rows.append(existing)
                else:
                    # Insert new record
                    memory_row = Memory(
                        category=memory["category"],
                        key=memory["key"],
                        value=memory["value"],
                        importance=memory["importance"],
                        source_conversation_id=conversation_id,
                    )
                    db.add(memory_row)
                    updated_rows.append(memory_row)

            db.commit()

            # Index every inserted or updated memory
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
