#this file is used to load the feature vectors store in .npy files into chromadb

import numpy as np
from config import FEATURES_PATH, IMAGE_PATHS_PATH
from utils.chroma_client import get_chroma_collection

def get_label_from_path(path: str) -> str:
    return path.split('/')[-2]

def load_embeddings_into_chroma():
    import time
    start = time.time()
    print("🔄 Loading features and image paths...")

    features = np.load(FEATURES_PATH)
    image_paths = np.load(IMAGE_PATHS_PATH)

    if len(features) != len(image_paths):
        raise ValueError("Mismatch between features and image paths")

    print(f"✅ Loaded {len(features)} features")

    collection = get_chroma_collection()

    ids = [f"img_{i}" for i in range(len(features))]
    embeddings = [features[i].tolist() for i in range(len(features))]
    metadatas = [{
        "url": str(image_paths[i]),
        "label": get_label_from_path(str(image_paths[i]))
    } for i in range(len(features))]

    # ✅ Batch insert to avoid Render crash
    batch_size = 500
    for i in range(0, len(features), batch_size):
        batch_ids = ids[i:i + batch_size]
        batch_embeddings = embeddings[i:i + batch_size]
        batch_metadatas = metadatas[i:i + batch_size]

        collection.add(
            ids=batch_ids,
            embeddings=batch_embeddings,
            metadatas=batch_metadatas
        )
        print(f"✅ Inserted {i + len(batch_ids)} / {len(features)} vectors")

    print(f"✅ Done. Total vectors: {len(features)}")
    print(f"⏱️ Total load time: {round(time.time() - start, 2)}s")
