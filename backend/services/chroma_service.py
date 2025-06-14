#this file is used to load the feature vectors store in .npy files into chromadb
import os
import numpy as np
from config import FEATURES_PATH, IMAGE_PATHS_PATH
from utils.chroma_client import get_chroma_collection

def get_label_from_path(path: str) -> str:

    return path.split('/')[-2]

def load_embeddings_into_chroma():

    features = np.load(FEATURES_PATH)
    image_paths = np.load(IMAGE_PATHS_PATH)

    if len(features) != len(image_paths):
        raise ValueError("Mismatch between features and image paths.")

    collection = get_chroma_collection()

    for i in range(len(features)):
        embedding = features[i].tolist()
        original_path = str(image_paths[i])
        label = get_label_from_path(original_path)
        filename = os.path.basename(original_path)

        url = f"data/resized/{label}/{filename}"

        collection.add(
            ids=[f"img_{i}"],
            embeddings=[embedding],
            metadatas=[{
                "url": url,
                "label": label
            }]
        )

        if i < 3:  # Optional: log first few
            print(f" img_{i}: {label} → {url}")

    print(f" Loaded {len(features)} vectors into ChromaDB.")
