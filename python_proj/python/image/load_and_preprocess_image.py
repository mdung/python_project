import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np

# ... rest of your script


def load_and_preprocess_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def classify_image(model, img_array):
    # Get model predictions
    predictions = model.predict(img_array)

    # Decode and print the top-3 predicted classes
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} ({score:.2f})")

if __name__ == "__main__":
    # Load the pre-trained MobileNetV2 model
    model = MobileNetV2(weights="imagenet")

    # Replace 'path/to/your/image.jpg' with the path to your image file
    image_path = 'img_src/t.jpg'

    # Load and preprocess the image
    img_array = load_and_preprocess_image(image_path)

    # Classify the image
    classify_image(model, img_array)
