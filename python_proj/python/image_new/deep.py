import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from deepdream import deep_dream
import os

class DeepDreamApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Deep Dream App")

        # Upload photo button
        self.upload_button = ttk.Button(self.master, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=20)

        # Generate deep dream button
        self.dream_button = ttk.Button(self.master, text="Generate Deep Dream", command=self.generate_deep_dream)
        self.dream_button.pack(pady=10)

        # Image display
        self.image_label = ttk.Label(self.master)
        self.image_label.pack(pady=20)

        # File path
        self.file_path = ""

    def upload_photo(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            self.display_image(self.file_path)

    def generate_deep_dream(self):
        if not self.file_path:
            tk.messagebox.showwarning("Warning", "Please upload a photo first.")
            return

        try:
            # Load the image
            image = Image.open(self.file_path)

            # Perform deep dream processing
            dream_image = deep_dream(image)

            # Display the deep dream image
            self.display_image_from_pil(dream_image)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error generating deep dream image: {str(e)}")

    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)

        # Update the image label
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def display_image_from_pil(self, pil_image):
        photo = ImageTk.PhotoImage(pil_image)

        # Update the image label
        self.image_label.configure(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = DeepDreamApp(root)
    root.mainloop()
