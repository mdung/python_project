import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
import streamlit as st
import requests
from PIL import Image

# Load pre-trained MobileNetV2 model from TensorFlow Hub
model_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
model = hub.load(model_url)

# Function to preprocess the image for the model
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Function to make predictions using the pre-trained model
def predict_image(img_path):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    return decoded_predictions

# Streamlit app
st.title("Plant and Animal Species Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # Make predictions when the user uploads an image
    if st.button("Classify"):
        with st.spinner("Classifying..."):
            image_path = "temp_image.jpg"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            predictions = predict_image(image_path)

            st.success("Classification completed!")

            # Display the top 3 predictions
            for i, (imagenet_id, label, score) in enumerate(predictions):
                st.write(f"{i + 1}: {label} ({score:.2f})")

# To run the app, save this code in a file, for example, `app.py`, and run the following command in your terminal:
# streamlit run app.py
