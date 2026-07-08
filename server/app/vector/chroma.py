from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parents[2]

DB_PATH = BASE_DIR / "vector_db"


class VectorDatabase:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(DB_PATH)
        )

        self.collection = self.client.get_or_create_collection(
            name="lifeos_memory"
        )