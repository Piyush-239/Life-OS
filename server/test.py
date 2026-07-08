from app.vector.chroma import VectorDatabase

db = VectorDatabase()

print(db.collection.count())
print(db.collection.get())