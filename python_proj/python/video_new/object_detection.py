import os
import tkinter as tk
from tkinter import filedialog
import cv2
from moviepy.editor import VideoFileClip

class ObjectDetectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Object Detection App")

        self.label = tk.Label(master, text="Upload Video:")
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload", command=self.upload_video)
        self.upload_button.pack()

        self.detect_button = tk.Button(master, text="Detect Objects", command=self.detect_objects)
        self.detect_button.pack()

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.video_path = file_path
            self.label.config(text=f"Uploaded Video: {os.path.basename(file_path)}")

    def detect_objects(self):
        if hasattr(self, 'video_path'):
            video_clip = VideoFileClip(self.video_path)

            # Load the object detection model from OpenCV
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            vehicle_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

            # Process each frame
            def process_frame(frame):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect human faces
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Detect vehicles
                vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
                for (x, y, w, h) in vehicles:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                return frame

            # Apply object detection to each frame
            processed_clip = video_clip.fl_image(process_frame)

            # Save the processed video
            output_path = self.get_output_path()
            processed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            processed_clip.close()

            self.label.config(text=f"Objects Detected! Saved as: {os.path.basename(output_path)}")
        else:
            self.label.config(text="Please upload a video first!")

    def get_output_path(self):
        input_filename = os.path.basename(self.video_path)
        output_filename = f"objects_detected_{os.path.splitext(input_filename)[0]}.mp4"
        output_path = os.path.join(os.path.dirname(self.video_path), output_filename)
        return output_path

def main():
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
