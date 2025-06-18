#  uvicorn main:app --reload -> we will run this command and start the api


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
# all route modules
from routes import search, extractor, preprocess, chroma_loader

app = FastAPI(title="AI Image Similarity Search")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
if os.path.exists("data/resized"):
    app.mount("/data", StaticFiles(directory="data"), name="data")

# Register all routers
app.include_router(search.router, prefix="/api")
app.include_router(preprocess.router, prefix="/api")
app.include_router(extractor.router, prefix="/api")
app.include_router(chroma_loader.router, prefix="/api")


# ✅ Root test endpoint
@app.get("/")
def root():
    return {"message": "Backend is running"}
