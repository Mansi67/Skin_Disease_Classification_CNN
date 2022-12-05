from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow import keras
from keras.applications.inception_v3 import preprocess_input
import numpy as np
from PIL import Image

skin_classes={0:"Acne", 1: "Eczema", 2:"Melanoma", 3:"Melasma", 4:"Psoriasis", 5:"Rosacea", 6:"Shingles", 7:"Urticaria"}
def getPrediction(filename):

    model = keras.models.load_model('C:/Users/mansi/Desktop/Study/Skin_Disease/FineTuning_InceptionResnet.h5')
    image = load_img('C:/Users/mansi/Desktop/Study/Skin_Disease/Uploads/'+filename, target_size=(299, 299))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    yhat = np.argmax(yhat, axis=1)
    pred=(skin_classes[int(yhat)])


    return pred
