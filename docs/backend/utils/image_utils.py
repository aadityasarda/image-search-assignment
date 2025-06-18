import numpy as np
from tf_keras.preprocessing import image
from tf_keras.applications.efficientnet import preprocess_input
from utils.model import get_model
from config import IMAGE_SIZE
from PIL import Image
from io import BytesIO

#this function will preprocess the uploaded image
def preprocess_image(file_bytes: bytes) -> np.ndarray:
    img = Image.open(BytesIO(file_bytes)).convert("RGB")
    img = img.resize(IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

#this function is used to get the embeddings of the upload image
def get_embedding(file_bytes: bytes) -> list:
    model = get_model()
    tensor = preprocess_image(file_bytes)
    vec = model.predict(tensor, verbose=0).flatten()
    vec = vec / np.linalg.norm(vec)
    return vec.tolist()