import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import waifu2x_ncnn_vulkan
import os

class PhotoEnhancerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Enhancer App")

        # Upload photo button
        self.upload_button = ttk.Button(self.master, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=20)

        # Enhance resolution button
        self.enhance_button = ttk.Button(self.master, text="Enhance Resolution", command=self.enhance_resolution)
        self.enhance_button.pack(pady=10)

        # Image display
        self.image_label = ttk.Label(self.master)
        self.image_label.pack(pady=20)

        # File path
        self.file_path = ""

    def upload_photo(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            self.display_image(self.file_path)

    def enhance_resolution(self):
        if not self.file_path:
            tk.messagebox.showwarning("Warning", "Please upload a photo first.")
            return

        try:
            # Load the image
            image = Image.open(self.file_path)

            # Convert to RGB if not already in that mode
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Perform image upscaling using waifu2x-ncnn-vulkan
            enhancer = waifu2x_ncnn_vulkan.Waifu2x()
            enhanced_image = enhancer.enhance(image)

            # Display the enhanced image
            self.display_image_from_pil(enhanced_image)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error enhancing resolution: {str(e)}")

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
    app = PhotoEnhancerApp(root)
    root.mainloop()
