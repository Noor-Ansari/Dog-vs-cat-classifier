from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image 
from tensorflow.keras.models import load_model 
import numpy as np
import tensorflow as tf

class Predict:
    def __init__(self):
        self.model = load_model('dog_cat_classifier.h5')
    def preprocess_img(self,image, target_size):
        self.image = image.resize(target_size)
        self.image = img_to_array(self.image)
        self.image = np.expand_dims(self.image, axis=0)
        self.image = tf.keras.applications.mobilenet.preprocess_input(self.image)
        return self.image 
