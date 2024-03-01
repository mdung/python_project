import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
from moviepy.editor import VideoClip, TextClip, CompositeVideoClip, concatenate_videoclips
import os
from pydub.utils import mediainfo

class AudioToVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio to Video App")

        self.audio_path = None
        self.output_path = None

        # Create widgets
        self.upload_audio_button = tk.Button(root, text="Upload Audio", command=self.upload_audio)
        self.upload_audio_button.pack(pady=10)

        self.generate_video_button = tk.Button(root, text="Generate Video", command=self.generate_video)
        self.generate_video_button.pack(pady=10)

    def upload_audio(self):
        self.audio_path = filedialog.askopenfilename(title="Select an Audio File",
                                                     filetypes=[("Audio files", "*.mp3;*.wav")])

    def generate_video(self):
        if self.audio_path:
            audio = AudioSegment.from_file(self.audio_path, format=mediainfo(self.audio_path)["format_name"])

            # Modify this function based on how you want to generate video from audio samples
            video_clip = self.create_video_from_audio(audio)

            self.output_path = self.get_output_path(self.audio_path)
            video_clip.write_videofile(self.output_path, codec="libx264", audio_codec="aac")

            tk.messagebox.showinfo("Video Generated", f"Video saved as:\n{self.output_path}")

    def create_video_from_audio(self, audio):
        # Placeholder implementation: Create a video with text displaying audio sample information
        # Modify this function based on your specific requirements

        samples = audio.split_to_mono()  # Split stereo audio to mono samples

        video_clips = []
        for i, sample in enumerate(samples):
            text = f"Audio Sample {i + 1}"
            text_clip = TextClip(text, fontsize=30, color="white", bg_color="black", size=(640, 480))
            audio_clip = AudioSegment.silent(duration=len(sample))
            video_clip = CompositeVideoClip([text_clip.set_audio(audio_clip), text_clip])
            video_clips.append(video_clip)

        final_clip = concatenate_videoclips(video_clips)
        return final_clip

    @staticmethod
    def get_output_path(input_path):
        # Modify this function to generate a meaningful output name based on the input file
        return "audio_to_video_" + os.path.basename(input_path).split(".")[0] + ".mp4"

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioToVideoApp(root)
    root.mainloop()
