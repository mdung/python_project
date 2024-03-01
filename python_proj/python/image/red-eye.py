import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def correct_red_eye(image_path):
    # Load image using OpenCV
    img = cv2.imread(image_path)

    # Convert BGR image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Perform red-eye correction (example: simple desaturation)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    img_rgb[:, :, 2] = cv2.subtract(img_rgb[:, :, 2], threshold)

    return Image.fromarray(img_rgb)

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Perform red-eye correction
        corrected_image = correct_red_eye(file_path)

        # Save the corrected image with a meaningful name
        output_file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                        filetypes=[("PNG files", "*.png"),
                                                                   ("JPEG files", "*.jpg;*.jpeg")])
        if output_file_path:
            corrected_image.save(output_file_path)
            update_image(output_file_path)

def update_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((400, 400))  # Resize image for display
    img = ImageTk.PhotoImage(img)
    image_label.configure(image=img)
    image_label.image = img

# Create the main window
app = tk.Tk()
app.title("Red-Eye Correction App")

# Create and configure the Upload button
upload_button = tk.Button(app, text="Upload Photo", command=upload_image)
upload_button.pack(pady=10)

# Create and configure the image label
image_label = tk.Label(app)
image_label.pack()

# Run the Tkinter main loop
app.mainloop()
