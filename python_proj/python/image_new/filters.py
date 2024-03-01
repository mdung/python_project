import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageFilter
import os

class PhotoFilterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Filter App")

        # Upload photo button
        self.upload_button = ttk.Button(self.master, text="Upload Photo", command=self.upload_photo)
        self.upload_button.pack(pady=20)

        # Filter selection dropdown
        self.filter_label = ttk.Label(self.master, text="Select Filter:")
        self.filter_label.pack(pady=5)

        self.filter_var = tk.StringVar()
        filters = ['BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EMBOSS', 'SHARPEN']
        self.filter_dropdown = ttk.Combobox(self.master, values=filters, textvariable=self.filter_var)
        self.filter_dropdown.pack(pady=10)
        self.filter_dropdown.set(filters[0])  # Set default filter

        # Apply Filter button
        self.apply_button = ttk.Button(self.master, text="Apply Filter", command=self.apply_filter)
        self.apply_button.pack(pady=10)

        # Image display
        self.image_label = ttk.Label(self.master)
        self.image_label.pack(pady=20)

        # File path
        self.file_path = ""

    def upload_photo(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            self.display_image(self.file_path)

    def apply_filter(self):
        if not self.file_path:
            tk.messagebox.showwarning("Warning", "Please upload a photo first.")
            return

        selected_filter = self.filter_var.get()

        try:
            image = Image.open(self.file_path)

            # Apply selected filter
            if selected_filter == 'BLUR':
                image = image.filter(ImageFilter.BLUR)
            elif selected_filter == 'CONTOUR':
                image = image.filter(ImageFilter.CONTOUR)
            elif selected_filter == 'DETAIL':
                image = image.filter(ImageFilter.DETAIL)
            elif selected_filter == 'EDGE_ENHANCE':
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif selected_filter == 'EMBOSS':
                image = image.filter(ImageFilter.EMBOSS)
            elif selected_filter == 'SHARPEN':
                image = image.filter(ImageFilter.SHARPEN)

            # Display the filtered image
            self.display_image_from_pil(image)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error applying filter: {str(e)}")

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
    app = PhotoFilterApp(root)
    root.mainloop()
