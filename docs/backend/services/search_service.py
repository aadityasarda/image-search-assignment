from utils.image_utils import get_embedding
from utils.chroma_client import get_chroma_collection
import numpy as np

def search_similar_images(file_bytes: bytes, top_k: int = 20) -> dict:

    query_vector = get_embedding(file_bytes)
    query_vector = query_vector / np.linalg.norm(query_vector)
    collection = get_chroma_collection()
    results = collection.query(query_embeddings=[query_vector], n_results=top_k)


    formatted = []
    for i in range(len(results["ids"][0])):
        metadata = results["metadatas"][0][i]
        distance = results["distances"][0][i]
        formatted.append({
            "rank": i + 1,
            "label": metadata.get("label", "unknown"),
            "url": metadata.get("url", ""),
            "score": round(distance, 4)
        })

    return {"results": formatted}