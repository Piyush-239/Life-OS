from app.vector.chroma import VectorDatabase
from app.vector.embedder import Embedder


class SemanticRetriever:

    def __init__(self):
        self.db = VectorDatabase()
        self.embedder = Embedder()

    def retrieve(self, query, top_k=5):

        embedding = self.embedder.encode(query)

        results = self.db.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        memories = []

        if results["metadatas"]:

            for metadata in results["metadatas"][0]:

                memories.append(
                    {
                        "category": metadata["category"],
                        "key": metadata["key"],
                        "value": metadata["value"],
                    }
                )

        return memories