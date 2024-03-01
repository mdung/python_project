import os
import shutil
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import uuid

class PhotoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Resizer")

        # Configure upload folder and allowed extensions
        self.upload_folder = 'uploads'
        self.allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}

        # Tkinter variables
        self.original_photo_path = tk.StringVar()
        self.result_photo_path = tk.StringVar()

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Label for displaying the original photo
        self.original_photo_label = tk.Label(self.master, text="Original Photo:")
        self.original_photo_label.pack()

        # Button to select and upload a photo
        self.upload_button = tk.Button(self.master, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack()

        # Label for displaying the result photo
        self.result_photo_label = tk.Label(self.master, text="Result Photo:")
        self.result_photo_label.pack()

        # Button to resize and crop the photo
        self.process_button = tk.Button(self.master, text="Resize and Crop", command=self.resize_and_crop)
        self.process_button.pack()

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.allowed_extensions

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Select a photo", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])

        if file_path:
            self.original_photo_path.set(file_path)

    def resize_and_crop(self):
        original_path = self.original_photo_path.get()

        if original_path and self.allowed_file(original_path):
            # Generate unique filenames
            filename = generate_filename(original_path)
            output_filename = generate_filename(original_path)

            # Save the original file
            file_path = os.path.join(self.upload_folder, filename)
            shutil.copy(original_path, file_path)

            # Resize and crop the image
            output_path = os.path.join(self.upload_folder, output_filename)
            self.resize_and_crop_image(file_path, output_path, (300, 300))

            # Display the result photo
            self.result_photo_path.set(output_path)
            self.display_result_photo(output_path)

    def resize_and_crop_image(self, image_path, output_path, size):
        original_image = Image.open(image_path)

        # Resize image while maintaining aspect ratio
        original_image.thumbnail(size, Image.ANTIALIAS)

        # Crop the center of the image
        width, height = original_image.size
        left = (width - size[0]) / 2
        top = (height - size[1]) / 2
        right = (width + size[0]) / 2
        bottom = (height + size[1]) / 2

        cropped_image = original_image.crop((left, top, right, bottom))
        cropped_image.save(output_path)

    def display_result_photo(self, path):
        result_image = Image.open(path)
        result_image.thumbnail((150, 150))
        result_photo = ImageTk.PhotoImage(result_image)

        result_label = tk.Label(self.master, image=result_photo)
        result_label.image = result_photo
        result_label.pack()

def generate_filename(filename):
    name, ext = os.path.splitext(filename)
    return f"{uuid.uuid4().hex}{ext}"

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root)
    root.mainloop()
