import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import dlib

class FacialRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Facial Recognition and Tagging App")

        self.image_path = None
        self.detected_faces = None

        # Create UI elements
        self.label = tk.Label(root, text="Upload Photo:")
        self.label.pack()

        self.upload_button = tk.Button(root, text="Upload", command=self.upload_image)
        self.upload_button.pack()

        self.detect_button = tk.Button(root, text="Detect Faces", command=self.detect_faces, state=tk.DISABLED)
        self.detect_button.pack()

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            self.image_path = file_path
            self.detect_button["state"] = tk.NORMAL
            self.display_image(self.image_path)

    def detect_faces(self):
        # Load the image
        image = cv2.imread(self.image_path)
        # Convert the image to RGB (OpenCV uses BGR by default)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Initialize the face detector from dlib
        face_detector = dlib.get_frontal_face_detector()
        # Detect faces in the image
        faces = face_detector(rgb_image)

        # Draw rectangles around detected faces
        for face in faces:
            left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

        # Save the result with a meaningful name
        output_file_name = "tagged_faces_" + filedialog.asksaveasfilename(defaultextension=".png",
                                                                          filetypes=[("PNG files", "*.png")])
        cv2.imwrite(output_file_name, cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        self.detected_faces = image
        self.display_image(output_file_name)

    def display_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image=image)

        self.canvas.config(width=photo.width(), height=photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = FacialRecognitionApp(root)
    root.mainloop()
