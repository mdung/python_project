import os
import tkinter as tk
from tkinter import filedialog
import cv2
from moviepy.editor import VideoFileClip
import dlib

class LipSyncApp:
    def __init__(self, master):
        self.master = master
        master.title("Lip Sync App")

        self.label = tk.Label(master, text="Upload Video:")
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload", command=self.upload_video)
        self.upload_button.pack()

        self.sync_button = tk.Button(master, text="Sync Lips", command=self.sync_lips)
        self.sync_button.pack()

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.video_path = file_path
            self.label.config(text=f"Uploaded Video: {os.path.basename(file_path)}")

    def sync_lips(self):
        if hasattr(self, 'video_path'):
            video_clip = VideoFileClip(self.video_path)

            # Load the facial landmark detector from dlib
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

            # Process each frame
            def process_frame(frame):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = detector(gray)

                if faces:
                    landmarks = predictor(gray, faces[0])
                    # TODO: Implement lip sync based on landmarks and audio processing
                    # Placeholder: Just draw a rectangle around the mouth
                    x, y, w, h = cv2.boundingRect(landmarks.parts()[48:68])
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                return frame

            # Apply lip sync to each frame
            processed_clip = video_clip.fl_image(process_frame)

            # Save the synced video
            output_path = self.get_output_path()
            processed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            processed_clip.close()

            self.label.config(text=f"Video Synced! Saved as: {os.path.basename(output_path)}")
        else:
            self.label.config(text="Please upload a video first!")

    def get_output_path(self):
        input_filename = os.path.basename(self.video_path)
        output_filename = f"lip_synced_{os.path.splitext(input_filename)[0]}.mp4"
        output_path = os.path.join(os.path.dirname(self.video_path), output_filename)
        return output_path

def main():
    root = tk.Tk()
    app = LipSyncApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
