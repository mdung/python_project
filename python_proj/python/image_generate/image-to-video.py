import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import dlib
import os
from datetime import datetime
from imutils import face_utils

class AvatarToVideoConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Avatar to Video Converter")

        self.file_path = tk.StringVar()
        self.video_output_path = ""

        # GUI Components
        self.label = tk.Label(self.master, text="Select Avatar Photo:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.convert_button = tk.Button(self.master, text="Convert to Video", command=self.convert_to_video)
        self.convert_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.file_path.set(file_path)
        self.display_image(file_path)

    def display_image(self, file_path):
        img = Image.open(file_path)
        img = img.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        if hasattr(self, 'panel'):
            self.panel.destroy()

        self.panel = tk.Label(self.master, image=img)
        self.panel.image = img
        self.panel.pack(pady=10)

    def convert_to_video(self):
        if not self.file_path.get():
            return

        image_path = self.file_path.get()
        video_output_path = self.get_output_path(image_path)

        img = cv2.imread(image_path)
        h, w, _ = img.shape

        # Use dlib to detect facial landmarks
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("D:/new_video/shape_predictor_68_face_landmarks.dat")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        if len(faces) == 0:
            messagebox.showwarning("Warning", "No face detected in the image.")
            return

        landmarks = predictor(gray, faces[0])

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(video_output_path, fourcc, 20, (w, h))

        for _ in range(100):  # 5 seconds video with 20 frames per second
            frame = img.copy()

            # Simulate natural head movement
            for i in range(68):
                landmarks.part(i).x += 10

            # Simulate natural lip movement
            for i in range(48, 68):
                landmarks.part(i).y += 10 * ((i - 48) % 3 - 1)  # Vary the movement based on the index

            # Draw the modified landmarks on the frame
            shape = face_utils.shape_to_np(landmarks)
            for (x, y) in shape:
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

            video_writer.write(frame)

        video_writer.release()

        self.display_success_message(video_output_path)

    def get_output_path(self, image_path):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"lip_sync_video_{timestamp}.mp4"
        self.video_output_path = os.path.join(os.path.dirname(image_path), file_name)
        return self.video_output_path

    def display_success_message(self, video_output_path):
        messagebox.showinfo("Success", f"Video saved at:\n{video_output_path}")

def main():
    root = tk.Tk()
    app = AvatarToVideoConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
