import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# Load the pre-trained model for image colorization
model = tf.keras.applications.MobileNetV2(input_shape=(None, None, 1),
                                          alpha=1.0,
                                          include_top=False,
                                          weights="imagenet")

def convert_to_color(input_path, output_path):
    # Load the image in grayscale
    grayscale_image = Image.open(input_path).convert("L")

    # Resize the image to fit the model input size
    input_array = np.expand_dims(np.array(grayscale_image), axis=-1) / 255.0
    input_array = tf.image.resize(input_array, (224, 224))
    input_array = np.expand_dims(input_array, axis=0)

    # Predict the colorized image using the model
    colorized_array = model.predict(input_array)

    # Save the colorized image
    colorized_image = tf.keras.preprocessing.image.array_to_img(colorized_array[0])
    colorized_image.save(output_path)

class PhotoColorizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Colorizer App")

        # Create widgets
        self.upload_button = tk.Button(root, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=20)

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.convert_button = tk.Button(root, text="Convert to Color", command=self.convert_to_color)
        self.convert_button.pack(pady=20)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.display_image(file_path)
            self.input_path = file_path

    def display_image(self, path):
        image = Image.open(path)
        image.thumbnail((300, 300))
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def convert_to_color(self):
        if hasattr(self, 'input_path'):
            output_path = self.generate_output_path(self.input_path)
            convert_to_color(self.input_path, output_path)
            output_message = f"Conversion complete! Saved as {os.path.basename(output_path)}"
            tk.messagebox.showinfo("Success", output_message)
        else:
            tk.messagebox.showerror("Error", "Please upload a photo first.")

    def generate_output_path(self, input_path):
        input_filename, input_extension = os.path.splitext(os.path.basename(input_path))
        output_filename = f"{input_filename}_colorized{input_extension}"
        output_path = filedialog.asksaveasfilename(defaultextension=input_extension, filetypes=[("Image files", f"*{input_extension}")], initialfile=output_filename)
        return output_path

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoColorizerApp(root)
    root.mainloop()
