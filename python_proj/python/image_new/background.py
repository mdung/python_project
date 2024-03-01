import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from removebg import RemoveBg
import os

class BackgroundRemoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Background Remover App")

        # Upload photo button
        self.upload_button = ttk.Button(self.master, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=20)

        # Remove background button
        self.remove_bg_button = ttk.Button(self.master, text="Remove Background", command=self.remove_background)
        self.remove_bg_button.pack(pady=10)

        # Image display
        self.image_label = ttk.Label(self.master)
        self.image_label.pack(pady=20)

        # File path
        self.file_path = ""

    def upload_photo(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            self.display_image(self.file_path)

    def remove_background(self):
        if not self.file_path:
            tk.messagebox.showwarning("Warning", "Please upload a photo first.")
            return

        try:
            # Load the image
            image = Image.open(self.file_path)

            # Remove background using removebg library
            remover = RemoveBg("YOUR_API_KEY", "error.log")  # Replace YOUR_API_KEY with your actual Remove.bg API key
            output_image = remover.remove_bg_file(self.file_path)

            # Display the image with the background removed
            self.display_image_from_pil(output_image)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error removing background: {str(e)}")

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
    app = BackgroundRemoverApp(root)
    root.mainloop()
