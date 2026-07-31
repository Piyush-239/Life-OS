from app.vector.chroma import VectorDatabase
from app.vector.embedder import Embedder
from app.memory.utils import normalize_key


class MemoryIndexer:

    def __init__(self):
        print("INDEXER CALLED")
        self.db = VectorDatabase()
        self.embedder = Embedder()

    def add(self, memory):

        text = (
            f"{memory.category} "
            f"{memory.key} "
            f"{memory.value}"
        )

        embedding = self.embedder.encode(text)

        # Use normalized key for the primary ID
        memory_id = f"{memory.category}:{normalize_key(memory.key)}"
        print(f"Indexing under ID: {memory_id}")
        print(f"Document text: {text}")

        # Delete any potential stale variations first
        try:
            self.db.collection.delete(
                ids=[
                    f"{memory.category}:{memory.key}",
                    memory_id,
                ]
            )
        except Exception as e:
            print(f"Chroma delete warning: {e}")

        # Upsert the updated memory
        self.db.collection.upsert(
            ids=[memory_id],
            embeddings=[embedding],
            documents=[text],
            metadatas=[
                {
                    "category": memory.category,
                    "key": memory.key,
                    "value": memory.value,
                }
            ],
        )
        print("UPSERT COMPLETE")
        print(f"Total documents in collection: {self.db.collection.count()}")