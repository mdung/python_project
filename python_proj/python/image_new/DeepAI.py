import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import requests
from io import BytesIO

class ColorizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Colorization App")

        self.image_path = ""

        self.create_widgets()

    def create_widgets(self):
        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)

        # Create the upload button
        upload_button = tk.Button(main_frame, text="Upload Photo", command=self.upload_photo)
        upload_button.grid(row=0, column=0, pady=10)

        # Create the colorize button
        colorize_button = tk.Button(main_frame, text="Colorize", command=self.colorize_photo)
        colorize_button.grid(row=0, column=1, pady=10)

        # Create the image display canvas
        self.image_canvas = tk.Canvas(main_frame, width=400, height=400)
        self.image_canvas.grid(row=1, column=0, columnspan=2)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)

        # Keep a reference to the image to prevent garbage collection
        self.image_canvas.photo = photo

        self.image_canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    def colorize_photo(self):
        if self.image_path:
            # Open the image using OpenCV
            image = cv2.imread(self.image_path)

            # Convert BGR to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Encode image to base64
            _, img_encoded = cv2.imencode(".png", image_rgb)
            img_base64 = BytesIO(img_encoded).read()

            # Send image to the DeepAI colorization API
            response = requests.post(
                "https://api.deepai.org/api/colorizer",
                files={"image": img_base64},
                headers={"api-key": "YOUR_DEEPAI_API_KEY"},
            )

            # Decode the response content
            colorized_image = Image.open(BytesIO(response.content))

            # Save colorized image with a meaningful name
            output_path = f"colorized_{self.get_file_name(self.image_path)}"
            colorized_image.save(output_path)

            # Display the colorized image
            self.display_image(output_path)

    @staticmethod
    def get_file_name(file_path):
        return file_path.split("/")[-1]

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorizationApp(root)
    root.mainloop()
