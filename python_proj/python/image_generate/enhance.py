import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageEnhancementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Enhancement App")

        self.original_image = None
        self.enhanced_image = None

        # Create UI elements
        self.label = tk.Label(root, text="Upload Photo:")
        self.label.pack()

        self.upload_button = tk.Button(root, text="Upload", command=self.upload_image)
        self.upload_button.pack()

        self.enhance_button = tk.Button(root, text="Enhance", command=self.enhance_image, state=tk.DISABLED)
        self.enhance_button.pack()

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image)
            self.enhance_button["state"] = tk.NORMAL

    def enhance_image(self):
        # Perform image enhancement here
        # You can use any image processing library like OpenCV or Pillow for enhancement
        # For a simple example, let's just convert the image to grayscale

        enhanced_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

        # Save the enhanced image with a meaningful name
        output_file_name = "enhanced_" + filedialog.asksaveasfilename(defaultextension=".png",
                                                                      filetypes=[("PNG files", "*.png")])
        cv2.imwrite(output_file_name, enhanced_image)

        self.enhanced_image = enhanced_image
        self.display_image(self.enhanced_image)

    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)

        self.canvas.config(width=photo.width(), height=photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEnhancementApp(root)
    root.mainloop()
