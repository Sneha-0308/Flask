# from flask import Flask, request
# import numpy as np
# from PIL import Image
# import tensorflow as tf

# app = Flask(__name__)

# # Load the machine learning model
# # model = tf.keras.models.load_model('path/to/model.h5')
# model = tf.keras.applications.MobileNetV2()

# # Define a route for accepting image uploads
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the file from the POST request
#     file = request.files['file']

#     # Read the image
#     image = Image.open(file.stream)

#     # Preprocess the image
#     image = image.resize((224, 224))
#     image = np.array(image) / 255.0
#     image = np.expand_dims(image, axis=0)

#     # Make a prediction with the model
#     prediction = model.predict(image)

#     # Return the prediction as a JSON response
#     return {'prediction': prediction.tolist()}

# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import load_img, img_to_array

# # Load image and resize to 224x224
# image = load_img('my_image.jpg', target_size=(224, 224))

# # Convert image to numpy array and normalize pixel values
# image_array = img_to_array(image)
# image_array = image_array / 255.0  # normalize to [0, 1]

# # Add an extra dimension to represent the batch size
# image_array = tf.expand_dims(image_array, 0)

# # Load the pre-trained model
# model = tf.keras.applications.MobileNetV2()

# # Pass the image through the model to get predictions
# predictions = model.predict(image_array)

# # Print the top prediction
# print(tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1))





from flask import Flask
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.applications.MobileNetV2()
@app.route('/predict', methods=['POST'])
def predict():
    # Load image and resize to 224x224
    image = load_img('file', target_size=(224, 224))

    # Convert image to numpy array and normalize pixel values
    image_array = img_to_array(image)
    image_array = image_array / 255.0  # normalize to [0, 1]

    # Add an extra dimension to represent the batch size
    image_array = tf.expand_dims(image_array, 0)



    # Pass the image through the model to get predictions
    predictions = model.predict(image_array)

    # Print the top prediction
    print(tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1))

