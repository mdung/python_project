import os
import tkinter as tk
from tkinter import filedialog
import cv2
from moviepy.editor import VideoFileClip

class LicensePlateDetectionApp:
    def __init__(self, master):
        self.master = master
        master.title("License Plate Detection App")

        self.label = tk.Label(master, text="Upload Video:")
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload", command=self.upload_video)
        self.upload_button.pack()

        self.detect_button = tk.Button(master, text="Detect License Plates", command=self.detect_license_plates)
        self.detect_button.pack()

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.video_path = file_path
            self.label.config(text=f"Uploaded Video: {os.path.basename(file_path)}")

    def detect_license_plates(self):
        if hasattr(self, 'video_path'):
            video_clip = VideoFileClip(self.video_path)

            # Load the license plate detection model from OpenCV
            plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

            # Process each frame
            def process_frame(frame):
                # Convert the frame to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect license plates with adjusted parameters
                plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(80, 80))

                # Draw rectangles around detected license plates
                for (x, y, w, h) in plates:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                return frame

            # Apply license plate detection to each frame
            processed_clip = video_clip.fl_image(process_frame)

            # Save the processed video
            output_path = self.get_output_path()
            processed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            processed_clip.close()

            self.label.config(text=f"License Plates Detected! Saved as: {os.path.basename(output_path)}")
        else:
            self.label.config(text="Please upload a video first!")

    def get_output_path(self):
        input_filename = os.path.basename(self.video_path)
        output_filename = f"plates_detected_{os.path.splitext(input_filename)[0]}.mp4"
        output_path = os.path.join(os.path.dirname(self.video_path), output_filename)
        return output_path

def main():
    root = tk.Tk()
    app = LicensePlateDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
