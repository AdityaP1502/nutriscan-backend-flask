# Import necessary libraries
import os

MODEL_PATH = os.environ.get("TF_MODEL") or "tf-model/model.h5"
from flask import Flask, render_template, request, jsonify, abort
import tensorflow_hub as hub
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Create a Flask application
app = Flask(__name__)

# Load the Keras model
model = load_model(MODEL_PATH, custom_objects={'KerasLayer':hub.KerasLayer})

# Define a function to preprocess the image for the model
def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to between 0 and 1
    return img_array

# Define the Flask route for the form
@app.route('/predict', methods=['POST'])
def index():
    class_labels = [
        'Baked Potato', 'Burger', 'Donut', 
        'Fries', 'Hot Dog', 'Pizza', 
        'Sandwich', 'Taco', 'Taquito'
    ]
    
    # Get the uploaded image file
    file = request.files['image']
    # Save the image to a temporary file
    img_path = 'temp_image.jpg'
    file.save(img_path)
    
    # Preprocess the image for the model
    processed_image = preprocess_image(img_path)
    
    # Make predictions using the model
    predictions = model.predict(processed_image)
    
    # Return the predictions as a JSON response
    result = {class_labels[i]: float(predictions[0][i]) for i in range(len(class_labels)) if float(predictions[0][i]) > 0.5}
    
    if len(result) == 0:
        abort(400, 'Model cannot classify the image properly.')
        
    return jsonify(result)

# Run the Flask application
if __name__ == '__main__':
    DEBUG_MODE = False if os.environ.get("PRODUCTION") =="false" else "true"
    app.run(debug=DEBUG_MODE, host='0.0.0.0', port=8080)