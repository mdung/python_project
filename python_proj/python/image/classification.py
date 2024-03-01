import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

class ImageClassificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Classification Tool")

        self.image_path = None
        self.classification_result = tk.StringVar()
        self.classification_result.set("Classification Result: ")

        # Load the pre-trained model
        self.model = tf.keras.applications.MobileNetV2(weights='imagenet')

        # UI components
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.load_image)
        self.browse_button.pack(pady=10)

        self.classify_button = tk.Button(root, text="Classify Image", command=self.classify_image)
        self.classify_button.pack(pady=10)

        self.result_label = tk.Label(root, textvariable=self.classification_result)
        self.result_label.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            self.image_path = file_path

            # Display the selected image
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo

    def classify_image(self):
        if not self.image_path:
            tk.messagebox.showwarning("Warning", "Please select an image first.")
            return

        # Load and preprocess the image for classification
        image = tf.keras.preprocessing.image.load_img(self.image_path, target_size=(224, 224))
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        image_array = tf.expand_dims(image_array, 0)
        image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)

        # Make predictions
        predictions = self.model.predict(image_array)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions.numpy())[0]

        # Display the top prediction
        top_prediction = decoded_predictions[0]
        class_name, _, confidence = top_prediction
        result_text = f"Classification Result: {class_name} ({round(confidence * 100, 2)}%)"
        self.classification_result.set(result_text)

        # Save the classified image with a meaningful name
        output_name = self.generate_output_name()
        output_path = f"{output_name}_classified.jpg"
        Image.open(self.image_path).save(output_path)

        tk.messagebox.showinfo("Success", f"Image classified and saved as {output_path}")

    def generate_output_name(self):
        if self.image_path:
            # Extract the meaningful name from the file path
            file_name = self.image_path.split("/")[-1].split(".")[0]
            return f"{file_name}_classified"
        else:
            return "output"

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageClassificationApp(root)
    root.mainloop()
