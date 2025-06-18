#this is used to create an API Route which provides an endpoint to resize the raw dataset into 224x224
#it will call the function resize dataset from preprocess_service and then wrap into an api

from fastapi import APIRouter, HTTPException
from services.preprocess_service import resize_dataset

router = APIRouter()

@router.post("/preprocess")
def preprocess_images():

    try:
        resize_dataset()
        return {"message": " Dataset resized and saved to data/resized"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Preprocessing failed: {str(e)}")
