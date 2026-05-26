import numpy as np
from tensorflow.keras.layers import TFSMLayer
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
from PIL import Image

model = TFSMLayer("api/models/blur_images/", call_endpoint="serving_default")
label_file = open('api/models/blur_images/label_classes.txt', 'r')
label_set = [ line.replace(' \n', '') for line in label_file ]

def predict(image):
    image = Image.open(image)
    image = image.resize((224, 224))

    image = np.array(image, dtype=np.float32)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    output = model(image)
    pred = list(output.values())[0]
    pred = np.argmax(pred, axis=1)
    pred = label_set[pred[0]]
    return pred