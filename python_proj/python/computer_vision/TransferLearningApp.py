import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

class TransferLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transfer Learning Image Classifier")

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
            try:
                self.model = load_model(model_path)
                messagebox.showinfo("Success", "Model loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load model: {str(e)}")

    def choose_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            image_data = Image.open(self.image_path)
            image_data = image_data.resize((224, 224), Image.ANTIALIAS)
            image_data = ImageTk.PhotoImage(image_data)
            self.image_label.config(image=image_data)
            self.image_label.image = image_data

    def classify_image(self):
        if self.model is None:
            messagebox.showerror("Error", "Please load a model first.")
            return

        if hasattr(self, 'image_path'):
            img = image.load_img(self.image_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            result = self.model.predict(img_array)
            decoded_predictions = decode_predictions(result, top=3)[0]

            prediction_str = "\n".join([f"{label}: {prob * 100:.2f}%" for (_, label, prob) in decoded_predictions])
            self.result_label.config(text=f"Top 3 Predictions:\n{prediction_str}")
        else:
            messagebox.showerror("Error", "Please choose an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransferLearningApp(root)
    root.mainloop()
