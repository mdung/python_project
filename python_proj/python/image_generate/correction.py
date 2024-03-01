import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ColorCorrectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Correction App")

        self.original_image = None
        self.corrected_image = None

        # Create UI elements
        self.label = tk.Label(root, text="Upload Photo:")
        self.label.pack()

        self.upload_button = tk.Button(root, text="Upload", command=self.upload_image)
        self.upload_button.pack()

        self.correct_button = tk.Button(root, text="Correct Colors", command=self.correct_colors, state=tk.DISABLED)
        self.correct_button.pack()

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image)
            self.correct_button["state"] = tk.NORMAL

    def correct_colors(self):
        # Perform color correction using OpenCV or any other image processing library
        # For a simple example, let's just equalize the histogram

        corrected_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2YCrCb)
        channels = cv2.split(corrected_image)
        channels[0] = cv2.equalizeHist(channels[0])
        corrected_image = cv2.merge(channels)
        corrected_image = cv2.cvtColor(corrected_image, cv2.COLOR_YCrCb2BGR)

        # Save the corrected image with a meaningful name
        output_file_name = "corrected_" + filedialog.asksaveasfilename(defaultextension=".png",
                                                                       filetypes=[("PNG files", "*.png")])
        cv2.imwrite(output_file_name, corrected_image)

        self.corrected_image = corrected_image
        self.display_image(self.corrected_image)

    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)

        self.canvas.config(width=photo.width(), height=photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorCorrectionApp(root)
    root.mainloop()
