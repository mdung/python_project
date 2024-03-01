import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

class VideoConversionApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Conversion App")

        self.label = tk.Label(master, text="Upload .MOV Video:")
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload", command=self.upload_video)
        self.upload_button.pack()

        self.convert_button = tk.Button(master, text="Convert to MP4", command=self.convert_to_mp4)
        self.convert_button.pack()

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mov")])
        if file_path:
            self.video_path = file_path
            self.label.config(text=f"Uploaded Video: {os.path.basename(file_path)}")

    def convert_to_mp4(self):
        if hasattr(self, 'video_path'):
            # Load the video clip
            video_clip = VideoFileClip(self.video_path)

            # Get the output file path
            output_path = self.get_output_path()

            # Write the video clip to mp4
            video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            video_clip.close()

            self.label.config(text=f"Video Converted! Saved as: {os.path.basename(output_path)}")
        else:
            self.label.config(text="Please upload a .MOV video first!")

    def get_output_path(self):
        input_filename = os.path.basename(self.video_path)
        output_filename = f"{os.path.splitext(input_filename)[0]}_converted.mp4"
        output_path = os.path.join(os.path.dirname(self.video_path), output_filename)
        return output_path

def main():
    root = tk.Tk()
    app = VideoConversionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
