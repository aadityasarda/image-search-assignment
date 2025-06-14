🔍 AI-Powered Image Similarity Search
```text
EfficientNetB0 + ChromaDB + FastAPI | Find visually similar images instantly.
```

🎓 About

```text
This project implements a high-performance image similarity search system using:
EfficientNetB0 for image feature extraction (1280-d embeddings)
ChromaDB for fast vector similarity search (cosine distance)
FastAPI for the backend API
```

🛠️ Tech Stack

```text
Python 3.12.11 #Don't use the currect python version as tensorflow is not supported by the latest versions     
FastAPI
Uvicorn
TensorFlow / tf-keras
EfficientNetB0
ChromaDB
NumPy, OpenCV, Pillow
```

📁 Folder Structure

```text
backend/
├── main.py                  
├── config.py                
├── requirements.txt
├── routes/
│   ├── preprocess.py        
│   ├── extractor.py         
│   ├── chroma_loader.py     
│   └── search.py             
├── services/
│   ├── preprocess_service.py
│   ├── extract_service.py
│   ├── chroma_service.py
│   └── search_service.py
├── utils/
│   ├── image_utils.py       
│   ├── model.py             
│   └── chroma_client.py     
└── data/
    ├── resized/             
    └── features/            
```
    
🔄 API Flow

```text
Preprocess raw dataset → resize images to 224x224
Extract Features → EfficientNetB0 creates 1280-d embeddings
Load ChromaDB → load embeddings into ChromaDB
Search → upload a query image, get top-N similar matches
```

🛋️ Setup & Installation

```text
git clone https://github.com/yourusername/image-search-backend
cd backend
uvicorn main:app --reload
```

📡 API Endpoints

```text
Endpoint              Method     Description

/api/preprocess        POST      Resize dataset images (run once)
/api/extract-features  POST      Extract embeddings (run once)
/api/load-chroma       POST      Load embeddings into ChromaDB (every server start)
/api/search            POST      Upload query image and search
```