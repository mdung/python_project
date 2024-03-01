# Import necessary libraries
import os
from pathlib import Path
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from PIL import Image
import shutil

# Load pre-trained ResNet50 model
model = keras.applications.resnet50.ResNet50(weights='imagenet')

def predict_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = preprocess_input(img_array)

    # Make a prediction
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0][0]

    return decoded_predictions[1]  # Return the predicted label

def organize_and_tag_photo_library(input_folder, output_folder):
    # Ensure output folder exists
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Iterate through images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)

            # Predict the content of the image
            predicted_label = predict_image(image_path)

            # Create a folder based on the predicted label (if it doesn't exist)
            label_folder = os.path.join(output_folder, predicted_label)
            Path(label_folder).mkdir(parents=True, exist_ok=True)

            # Move the image to the corresponding folder
            shutil.move(image_path, os.path.join(label_folder, filename))

if __name__ == "__main__":
    # Specify the path to the input photo library and the output folder
    input_folder_path = "D:/OrganizedImages/JPEG_Images"
    output_folder_path = "C:/pto"

    # Organize and tag the photo library
    organize_and_tag_photo_library(input_folder_path, output_folder_path)
