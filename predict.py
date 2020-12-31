from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image 
from tensorflow.keras.models import load_model 
import numpy as np

class Predict:
    def __init__(self):
        self.model = load_model('dog_cat_classifier.h5')
    def preprocess_img(self,image, target_size):
        image = image.resize(target_size)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = tensorflow.keras.applications.mobilenet.preprocess_input(image)
        return image 