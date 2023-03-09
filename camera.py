import json
from keras.utils import load_img,img_to_array
from PIL import Image
from flask import Flask, jsonify, request
import tensorflow as tf
import numpy as np
# from keras.preprocessing.image import 

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.applications.MobileNetV2()
@app.route('/predict', methods=['POST'])
def predict():
    # get the file from POST
    file = request.files['file']
    # print(file)
    image = Image.open(file.stream)

    #image preprocessing
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)



    # Pass the image through the model to get predictions
    predictions = model.predict(image)
    result=tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    return jsonify({'result':json.dumps(str(result))})

if __name__ == "__main__":
    app.run(debug=True)