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

            # Process each frame
            def process_frame(frame):
                # Detect vehicles
                vehicle_frame = self.detect_vehicles(frame)

                # Detect animals
                animal_frame = self.detect_animals(frame)

                # Combine the results
                result_frame = cv2.addWeighted(vehicle_frame, 1, animal_frame, 1, 0)

                return result_frame

            # Apply object detection to each frame
            processed_clip = video_clip.fl_image(process_frame)

            # Save the processed video
            output_path = self.get_output_path()
            processed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            processed_clip.close()

            self.label.config(text=f"Objects Detected! Saved as: {os.path.basename(output_path)}")
        else:
            self.label.config(text="Please upload a video first!")

    def detect_vehicles(self, frame):
        # Load the vehicle detection model from OpenCV (Haar Cascade)
        vehicle_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles
        vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        # Draw rectangles around detected vehicles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return frame

    def detect_animals(self, frame):
        # Simple color-based segmentation for animal detection (replace with a more sophisticated algorithm if needed)
        lower_green = (40, 50, 40)
        upper_green = (80, 255, 255)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Find contours of green regions
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw rectangles around detected animals
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame

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
