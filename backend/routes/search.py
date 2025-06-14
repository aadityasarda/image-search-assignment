#this API route provides an endpoint to search for similar images based on a single uploaded query image.

from fastapi import APIRouter, UploadFile, File, HTTPException
from services.search_service import search_similar_images

router = APIRouter()

@router.post("/search")
async def search(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        response = search_similar_images(image_bytes, top_k=5)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")