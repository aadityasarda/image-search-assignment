#this API route provides an endpoint to load precomputed image embeddings and their paths into chromaDB.

from fastapi import APIRouter, HTTPException
from services.chroma_service import load_embeddings_into_chroma

router = APIRouter()

@router.post("/load-chroma")
def load_chroma():

    try:
        load_embeddings_into_chroma()
        return {"message": " Embeddings successfully loaded into ChromaDB."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ChromaDB load failed: {str(e)}")
