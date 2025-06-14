IMAGE_SIZE = (224, 224) #resized image pixels define here
EMBEDDING_SIZE = 1280 # # Number of features in each vector from EfficientNetB0

RESIZED_IMAGE_DIR = r"F:\Users\Vinnu\PycharmProjects\image-search-assignment\backend\data\resized"
FEATURES_PATH = r"F:\Users\Vinnu\PycharmProjects\image-search-assignment\backend\data\features\efficientnet_features.npy"
IMAGE_PATHS_PATH = r"F:\Users\Vinnu\PycharmProjects\image-search-assignment\backend\data\features\efficientnet_paths.npy"

CHROMA_DB_DIR = "data/chroma_db" #directory to store ChromaDB persistent data
CHROMA_COLLECTION_NAME = "image_vectors"#ChromaDB collection name to store image vectors