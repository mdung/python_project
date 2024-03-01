import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

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

            # TODO: Implement lip sync algorithm here

            # Save the synced video
            output_path = self.get_output_path()
            video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            video_clip.close()

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
