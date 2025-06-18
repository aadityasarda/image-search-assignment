#this API route provides an endpoint to extract 1280-d embeddings from preprocessed images using efficientnet

from fastapi import APIRouter, HTTPException
from services.extract_service import extract_features_from_dataset

router = APIRouter()

@router.post("/extract-features")
def extract_features():

    try:
        extract_features_from_dataset()
        return {"message": " Feature extraction complete and saved as .npy files."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Feature extraction failed: {str(e)}")
