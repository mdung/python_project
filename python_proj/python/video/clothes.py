import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ClothingChangeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clothing Change App")

        self.image_path = None
        self.output_path = None

        # Create widgets
        self.upload_button = tk.Button(root, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=10)

        self.change_clothing_button = tk.Button(root, text="Change Clothing", command=self.change_clothing)
        self.change_clothing_button.pack(pady=10)

    def upload_photo(self):
        self.image_path = filedialog.askopenfilename(title="Select an Image File",
                                                     filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        # Display the uploaded photo
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            label = tk.Label(root, image=img)
            label.image = img
            label.pack(pady=10)

    def change_clothing(self):
        if self.image_path:
            image = cv2.imread(self.image_path)

            # Apply clothing change or any desired image processing here
            # For simplicity, we will just replace a specific color with another color
            new_clothing_color = [0, 0, 255]  # New clothing color (BGR format)
            mask = self.create_clothing_mask(image)

            # Replace the color in the clothing region
            image[mask] = new_clothing_color

            # Save the processed image with a meaningful name
            self.output_path = self.get_output_path(self.image_path)
            cv2.imwrite(self.output_path, image)
            tk.messagebox.showinfo("Clothing Change", f"Clothing changed photo saved as:\n{self.output_path}")

    def create_clothing_mask(self, image):
        # Replace this function with a more advanced method for detecting clothing
        # For simplicity, we will create a mask based on a specific color range (e.g., blue)
        lower_bound = np.array([100, 0, 0])
        upper_bound = np.array([140, 255, 255])
        mask = cv2.inRange(image, lower_bound, upper_bound)

        return mask

    @staticmethod
    def get_output_path(input_path):
        # Modify this function to generate a meaningful output name based on the input file
        return "clothing_changed_" + input_path.split("/")[-1]

if __name__ == "__main__":
    root = tk.Tk()
    app = ClothingChangeApp(root)
    root.mainloop()
