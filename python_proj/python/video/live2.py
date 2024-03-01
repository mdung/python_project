import tkinter as tk
from tkinter import filedialog
import cv2
from moviepy.editor import VideoFileClip
import os

class LipSyncApp:
    def __init__(self, master):
        self.master = master
        master.title("Lip Sync App")

        # Create labels
        self.avatar_label = tk.Label(master, text="Avatar:")
        self.audio_label = tk.Label(master, text="Audio:")

        # Create buttons
        self.avatar_button = tk.Button(master, text="Upload Avatar", command=self.upload_avatar)
        self.audio_button = tk.Button(master, text="Upload Audio", command=self.upload_audio)
        self.sync_button = tk.Button(master, text="Create Lip Sync", command=self.create_lip_sync)

        # Layout
        self.avatar_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.audio_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.avatar_button.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.audio_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.sync_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Initialize file paths
        self.avatar_path = ""
        self.audio_path = ""

    def upload_avatar(self):
        self.avatar_path = filedialog.askopenfilename(title="Select Avatar Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    def upload_audio(self):
        self.audio_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio files", "*.mp3")])

    def create_lip_sync(self):
        if not self.avatar_path or not self.audio_path:
            return

        # Load avatar image
        avatar = cv2.imread(self.avatar_path)

        # Extract audio from video file
        video_clip = VideoFileClip(self.audio_path)
        audio_clip = video_clip.audio

        # Set the frame rate for the video clip
        video_clip = video_clip.set_audio(audio_clip).set_duration(audio_clip.duration)

        # Create lip-sync video
        output_filename = self.generate_output_filename()
        video_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")

        # Display success message
        tk.messagebox.showinfo("Success", f"Lip-sync video created: {output_filename}")

    def generate_output_filename(self):
        avatar_name = os.path.splitext(os.path.basename(self.avatar_path))[0]
        audio_name = os.path.splitext(os.path.basename(self.audio_path))[0]
        return f"LipSync_{avatar_name}_{audio_name}.mp4"


if __name__ == "__main__":
    root = tk.Tk()
    app = LipSyncApp(root)
    root.mainloop()
