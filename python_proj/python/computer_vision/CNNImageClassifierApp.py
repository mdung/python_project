import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class CNNImageClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CNN Image Classifier")

        self.load_model_button = tk.Button(self.root, text="Load Model", command=self.load_model)
        self.load_model_button.pack(pady=10)

        self.choose_image_button = tk.Button(self.root, text="Choose Image", command=self.choose_image)
        self.choose_image_button.pack(pady=10)

        self.classify_button = tk.Button(self.root, text="Classify Image", command=self.classify_image)
        self.classify_button.pack(pady=10)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.model = None

    def load_model(self):
        model_path = filedialog.askopenfilename(filetypes=[("Model files", "*.h5")])
        if model_path:
            self.model = load_model(model_path)
            messagebox.showinfo("Success", "Model loaded successfully!")

    def choose_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            image_data = Image.open(self.image_path)
            image_data = image_data.resize((250, 250), Image.ANTIALIAS)
            image_data = ImageTk.PhotoImage(image_data)
            self.image_label.config(image=image_data)
            self.image_label.image = image_data

    def classify_image(self):
        if self.model is None:
            messagebox.showerror("Error", "Please load a model first.")
            return

        if hasattr(self, 'image_path'):
            img = image.load_img(self.image_path, target_size=(64, 64))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            result = self.model.predict(img_array)
            class_index = np.argmax(result)

            classes = ["Class 0", "Class 1"]  # Replace with your actual class labels

            self.result_label.config(text=f"Predicted Class: {classes[class_index]}")
        else:
            messagebox.showerror("Error", "Please choose an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CNNImageClassifierApp(root)
    root.mainloop()
