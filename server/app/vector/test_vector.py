from app.vector.embedder import Embedder
from app.vector.chroma import VectorDatabase

embedder = Embedder()

vector_db = VectorDatabase()

embedding = embedder.encode(
    "favorite_drink coffee"
)

print(len(embedding))

print(vector_db.collection.count())