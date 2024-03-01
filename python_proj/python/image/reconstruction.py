import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def inpaint_image(image_path, mask_path):
    # Load the image and mask using OpenCV
    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # Perform inpainting
    inpainted_image = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    return Image.fromarray(cv2.cvtColor(inpainted_image, cv2.COLOR_BGR2RGB))

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        mask_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if mask_path:
            # Perform inpainting
            inpainted_image = inpaint_image(file_path, mask_path)

            # Save the inpainted image with a meaningful name
            output_file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                            filetypes=[("PNG files", "*.png"),
                                                                       ("JPEG files", "*.jpg;*.jpeg")])
            if output_file_path:
                inpainted_image.save(output_file_path)
                update_image(output_file_path)

def update_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((400, 400))  # Resize image for display
    img = ImageTk.PhotoImage(img)
    image_label.configure(image=img)
    image_label.image = img

# Create the main window
app = tk.Tk()
app.title("Image Inpainting App")

# Create and configure the Upload button
upload_button = tk.Button(app, text="Upload Photo", command=upload_image)
upload_button.pack(pady=10)

# Create and configure the image label
image_label = tk.Label(app)
image_label.pack()

# Run the Tkinter main loop
app.mainloop()
