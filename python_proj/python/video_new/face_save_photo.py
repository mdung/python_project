import os
import tkinter as tk
from tkinter import filedialog
import cv2
from moviepy.editor import VideoFileClip

class FaceRecognitionApp:
    def __init__(self, master):
        self.master = master
        master.title("Face Recognition App")

        self.label = tk.Label(master, text="Upload Video:")
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload", command=self.upload_video)
        self.upload_button.pack()

        self.detect_button = tk.Button(master, text="Detect and Register Faces", command=self.detect_and_register_faces)
        self.detect_button.pack()

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.video_path = file_path
            self.label.config(text=f"Uploaded Video: {os.path.basename(file_path)}")

    def detect_and_register_faces(self):
        if hasattr(self, 'video_path'):
            video_clip = VideoFileClip(self.video_path)

            # Load the face detection model from OpenCV
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Create a folder for registered faces
            output_folder = self.create_output_folder()

            # Process each frame
            def process_frame(frame):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                # Draw rectangles around detected faces and save registered faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    # Crop the face region
                    face_region = frame[y:y + h, x:x + w]

                    # Save the registered face
                    self.save_registered_face(face_region, output_folder)

                return frame

            # Apply face detection to each frame
            processed_clip = video_clip.fl_image(process_frame)

            # Save the processed video
            output_path = self.get_output_path()
            processed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            processed_clip.close()

            self.label.config(text=f"Faces Detected and Registered! Saved as: {os.path.basename(output_path)}")
        else:
            self.label.config(text="Please upload a video first!")

    def create_output_folder(self):
        input_filename = os.path.basename(self.video_path)
        folder_name = f"registered_faces_{os.path.splitext(input_filename)[0]}"
        output_folder = os.path.join(os.path.dirname(self.video_path), folder_name)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        return output_folder

    def save_registered_face(self, face_region, output_folder):
        # Generate a unique filename for each registered face
        face_filename = f"registered_face_{len(os.listdir(output_folder)) + 1}.png"
        face_path = os.path.join(output_folder, face_filename)

        # Save the registered face as an image
        cv2.imwrite(face_path, face_region)

    def get_output_path(self):
        input_filename = os.path.basename(self.video_path)
        output_filename = f"faces_detected_{os.path.splitext(input_filename)[0]}.mp4"
        output_path = os.path.join(os.path.dirname(self.video_path), output_filename)
        return output_path

def main():
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
