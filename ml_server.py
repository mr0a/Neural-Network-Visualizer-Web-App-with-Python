# Creating file and writing it from jupyter

import json 
import tensorflow as tf
import random
import numpy as np

from flask import Flask, request

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5')
# This model will give final predictions but not the values of hidden layers
# Create another model with keras api which gives the output of all layers too
feature_model = tf.keras.models.Model(
    model.inputs, # input
    [layer.output for layer in model.layers] #List of Output of all layers as output
)

_, (x_test, _) = tf.keras.datasets.mnist.load_data()
x_test = x_test / 255. # Normalizing
# we need to visualize this so no reshaping

def get_predictions():
    index = np.random.choice(x_test.shape[0]) # Choosing 1 from all available
    image = x_test[index, :, :]
    image_arr = np.reshape(image, (1, 784))
    return feature_model.predict(image_arr), image #Sending image & prediction


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        preds, image = get_predictions()
        # Json can send list and not numpy arrays
        final_preds = [p.tolist() for p in preds] # Numpy to list
        return json.dumps({
            'prediction': final_preds,
            'image': image.tolist()
        })
    return "Welcome to the ML Server"


if __name__ == "__main__":
    app.run()
    
