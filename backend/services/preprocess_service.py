# in this we are taking each and image and resized to the 224x224 which is defined in config.py, and we just import that

import os
import cv2
from config import RESIZED_IMAGE_DIR
from pathlib import Path

def resize_dataset(input_dir: str = r"F:\Users\Vinnu\PycharmProjects\image-search-assignment\dataset\train"):
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Dataset folder '{input_dir}' not found.")

    Path(RESIZED_IMAGE_DIR).mkdir(parents=True, exist_ok=True)

    for class_name in os.listdir(input_dir):
        class_path = os.path.join(input_dir, class_name)
        save_class_path = os.path.join(RESIZED_IMAGE_DIR, class_name)
        os.makedirs(save_class_path, exist_ok=True)

        for image_name in os.listdir(class_path):
            img_path = os.path.join(class_path, image_name)
            img = cv2.imread(img_path)

            if img is None:
                print(f" Skipping unreadable: {img_path}")
                continue

            resized = cv2.resize(img, (224, 224))
            save_path = os.path.join(save_class_path, image_name)
            cv2.imwrite(save_path, resized)

    print(f"Images resized from '{input_dir}' to '{RESIZED_IMAGE_DIR}'.")
