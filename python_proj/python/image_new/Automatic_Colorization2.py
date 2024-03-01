import tkinter as tk
from tkinter import filedialog

import cv2
from PIL import Image, ImageTk
import torch
from torchvision import models, transforms
import numpy as np

class ColorizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Colorization App")

        self.image_path = ""

        self.create_widgets()

    def create_widgets(self):
        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)

        # Create the upload button
        upload_button = tk.Button(main_frame, text="Upload Photo", command=self.upload_photo)
        upload_button.grid(row=0, column=0, pady=10)

        # Create the colorize button
        colorize_button = tk.Button(main_frame, text="Colorize", command=self.colorize_photo)
        colorize_button.grid(row=0, column=1, pady=10)

        # Create the image display canvas
        self.image_canvas = tk.Canvas(main_frame, width=400, height=400)
        self.image_canvas.grid(row=1, column=0, columnspan=2)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)

        # Keep a reference to the image to prevent garbage collection
        self.image_canvas.photo = photo

        self.image_canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    def colorize_photo(self):
        if self.image_path:
            # Open the image using OpenCV
            image = cv2.imread(self.image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Resize image to fit the Colorful Image Colorization model
            image = cv2.resize(image, (224, 224))

            # Convert image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

            # Convert to PyTorch tensor
            gray_tensor = transforms.ToTensor()(gray_image).unsqueeze(0)

            # Use a pre-trained model for colorization
            model = models.resnet18()
            model.load_state_dict(torch.load("colorization_model.pth", map_location=torch.device("cpu")))
            model.eval()

            with torch.no_grad():
                output_ab = model(gray_tensor)

            # Rescale the colorized AB channels
            output_ab = output_ab.squeeze().numpy()
            output_ab = (output_ab + 1.0) * 50.0

            # Create the colorized LAB image
            colorized_lab_image = np.concatenate([gray_image[:, :, np.newaxis], output_ab], axis=-1)

            # Convert the colorized LAB image back to RGB
            colorized_image = cv2.cvtColor(colorized_lab_image.astype(np.uint8), cv2.COLOR_LAB2RGB)

            # Display the colorized image
            colorized_image = Image.fromarray(colorized_image)
            self.display_image_from_array(colorized_image)

    def display_image_from_array(self, array_image):
        array_image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(array_image)

        # Keep a reference to the image to prevent garbage collection
        self.image_canvas.photo = photo

        self.image_canvas.create_image(0, 0, anchor=tk.NW, image=photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorizationApp(root)
    root.mainloop()
