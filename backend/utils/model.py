#to load the model and then use of single instance of efficientnet model
from tf_keras.applications import EfficientNetB0
from tf_keras.models import Model

_model = None

def get_model() -> Model:
    global _model
    if _model is None:
        _model = EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')
    return _model