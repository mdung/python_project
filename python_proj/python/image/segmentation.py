import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageSegmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Segmentation Tool")

        self.image_path = None
        self.output_path = None

        # UI components
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.load_image)
        self.browse_button.pack(pady=10)

        self.segment_button = tk.Button(root, text="Segment Image", command=self.segment_image)
        self.segment_button.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            self.image_path = file_path

            # Display the selected image
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo

    def segment_image(self):
        if not self.image_path:
            tk.messagebox.showwarning("Warning", "Please select an image first.")
            return

        # Image segmentation logic (you can replace this with your own segmentation algorithm)
        input_image = cv2.imread(self.image_path)
        gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

        # Save the segmented image
        output_name = self.generate_output_name()
        self.output_path = f"{output_name}_segmented.jpg"
        cv2.imwrite(self.output_path, binary_image)

        tk.messagebox.showinfo("Success", f"Image segmented and saved as {self.output_path}")

    def generate_output_name(self):
        if self.image_path:
            # Extract the meaningful name from the file path
            file_name = self.image_path.split("/")[-1].split(".")[0]
            return f"{file_name}_segmented"
        else:
            return "output"

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSegmentationApp(root)
    root.mainloop()
