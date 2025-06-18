# this is used to take the resized images and convert them to feature vectors and then store them into efficient_features.npy and efficientnet_paths.npy

import os
import numpy as np
from tf_keras.preprocessing import image
from tf_keras.applications.efficientnet import preprocess_input
from config import RESIZED_IMAGE_DIR, FEATURES_PATH, IMAGE_PATHS_PATH, IMAGE_SIZE
from utils.model import get_model
from tqdm import tqdm

def extract_features_from_dataset():
    if not os.path.exists(RESIZED_IMAGE_DIR):
        raise FileNotFoundError(f"Resized images folder '{RESIZED_IMAGE_DIR}' not found.")

    model = get_model()
    features = []
    image_paths = []

    for class_name in os.listdir(RESIZED_IMAGE_DIR):
        class_path = os.path.join(RESIZED_IMAGE_DIR, class_name)

        for img_name in tqdm(os.listdir(class_path), desc=f"Extracting: {class_name}"):
            img_path = os.path.join(class_path, img_name)
            try:
                img = image.load_img(img_path, target_size=IMAGE_SIZE)
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = preprocess_input(x)

                vec = model.predict(x, verbose=0).flatten()
                vec = vec / np.linalg.norm(vec)  # Normalize for cosine similarity

                features.append(vec)
                image_paths.append(img_path)

            except Exception as e:
                print(f" Error processing {img_path}: {e}")
                continue

    # Save results
    np.save(FEATURES_PATH, np.array(features).astype('float32'))
    np.save(IMAGE_PATHS_PATH, np.array(image_paths))
    print(f" Saved {len(features)} embeddings to '{FEATURES_PATH}'")
