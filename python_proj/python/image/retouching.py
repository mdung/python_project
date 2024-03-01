import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageFilter
import os

class PhotoProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Processing Tool")

        self.create_widgets()

    def create_widgets(self):
        # Upload Photo Button
        upload_button = tk.Button(self.root, text="Upload Photo", command=self.upload_photo)
        upload_button.pack(pady=10)

        # Process Photo Button
        process_button = tk.Button(self.root, text="Process Photo", command=self.process_photo)
        process_button.pack(pady=10)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Select a photo",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        self.photo_path = file_path
        print("Photo selected:", file_path)

    def process_photo(self):
        if not hasattr(self, 'photo_path'):
            print("Please upload a photo first.")
            return

        # Open the image using Pillow
        image = Image.open(self.photo_path)

        # Example processing: Enhance the image
        enhanced_image = ImageEnhance.Contrast(image).enhance(1.5)
        enhanced_image = enhanced_image.filter(ImageFilter.SHARPEN)

        # Get the base name of the uploaded file (without the path)
        base_name = os.path.basename(self.photo_path)

        # Create a meaningful name for the output file
        output_file_name = f"processed_{base_name}"

        # Save the processed image
        output_path = os.path.join(os.path.dirname(self.photo_path), output_file_name)
        enhanced_image.save(output_path)

        print(f"Photo processed and saved as: {output_file_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoProcessingApp(root)
    root.mainloop()
