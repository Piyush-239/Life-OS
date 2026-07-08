from app.vector.chroma import VectorDatabase
from app.vector.embedder import Embedder


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

        memory_id = (
            f"{memory.category}:"
            f"{memory.key}"
        )
        print(memory_id)
        print(text)
        print(len(embedding))

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

        print(self.db.collection.count())