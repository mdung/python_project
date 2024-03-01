# Install necessary packages
# pip install Flask tensorflow opencv-python

# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained deep learning model for image classification
model = load_model('your_medical_image_model.h5')

# Define a function to preprocess the input image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Define route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for image upload and analysis
@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    # Get the uploaded image file
    uploaded_file = request.files['image']

    # Save the uploaded image
    image_path = 'C:/pto'
    uploaded_file.save(image_path)

    # Preprocess the uploaded image
    processed_image = preprocess_image(image_path)

    # Perform prediction using the model
    predictions = model.predict(processed_image)

    # Get the predicted class
    predicted_class = np.argmax(predictions)

    # Map predicted class to a human-readable label (you need to define this)
    disease_label = get_disease_label(predicted_class)

    # Return the prediction result as a JSON response
    return jsonify({'result': disease_label})

# Define a function to map predicted class to a human-readable label
def get_disease_label(predicted_class):
    # You need to define the mapping based on your specific application
    # For example, you might have a dictionary mapping class indices to disease names
    disease_mapping = {0: 'Normal', 1: 'Cancer', 2: 'Other Disease'}
    return disease_mapping.get(predicted_class, 'Unknown')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
