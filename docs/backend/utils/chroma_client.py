from chromadb import Client
from chromadb.config import Settings
from config import CHROMA_DB_DIR, CHROMA_COLLECTION_NAME

#in this we are creating the chroma collection if it is not present or will use the existing collection
#this collection stores the feature vectors of images
def get_chroma_collection():
    client = Client(Settings(
        persist_directory=CHROMA_DB_DIR,
        anonymized_telemetry=False
    ))

    try:
        collection = client.get_collection(name=CHROMA_COLLECTION_NAME)
    except:
        collection = client.create_collection(name="image_vectors",
    metadata={"hnsw:space": "cosine"})

    return collection
