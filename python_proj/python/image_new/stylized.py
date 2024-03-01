import tkinter as tk
from tkinter import ttk, filedialog

import requests
from PIL import Image, ImageTk
import openai
import os

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

class PhotoStylizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Stylizer App")

        # Upload photo button
        self.upload_button = ttk.Button(self.master, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=20)

        # Stylize button
        self.stylize_button = ttk.Button(self.master, text="Generate Stylized Photo", command=self.generate_stylized_photo)
        self.stylize_button.pack(pady=10)

        # Image display
        self.image_label = ttk.Label(self.master)
        self.image_label.pack(pady=20)

        # File path
        self.file_path = ""

    def upload_photo(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            self.display_image(self.file_path)

    def generate_stylized_photo(self):
        if not self.file_path:
            tk.messagebox.showwarning("Warning", "Please upload a photo first.")
            return

        try:
            with open(self.file_path, "rb") as file:
                file_content = file.read()

            # Call the OpenAI API to generate a stylized image
            response = openai.Image.create(
                model="image-alpha-001",
                files={"image": file_content}
            )

            # Get the generated image URL
            image_url = response['url']

            # Display the stylized image
            self.display_image_from_url(image_url)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error generating stylized photo: {str(e)}")

    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)

        # Update the image label
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def display_image_from_url(self, image_url):
        image = Image.open(requests.get(image_url, stream=True).raw)
        photo = ImageTk.PhotoImage(image)

        # Update the image label
        self.image_label.configure(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoStylizerApp(root)
    root.mainloop()
