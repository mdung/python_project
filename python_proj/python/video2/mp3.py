import os
from tkinter import Tk, Label, Button, filedialog
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment

def upload_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    video_label.config(text=f"Video selected: {os.path.basename(video_path)}")
    return video_path

def upload_audio():
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3")])
    audio_label.config(text=f"Audio selected: {os.path.basename(audio_path)}")
    return audio_path

def combine_files():
    video_path = upload_video()
    audio_path = upload_audio()

    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        combined_clip = video_clip.set_audio(audio_clip)

        # Create a default output file name based on input files
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        audio_name = os.path.splitext(os.path.basename(audio_path))[0]
        output_path = f"{video_name}_with_{audio_name}.mp4"

        combined_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        info_label.config(text=f"Video created successfully at:\n{output_path}")
    except Exception as e:
        info_label.config(text=f"Error: {str(e)}")

# Create a Tkinter window
root = Tk()
root.title("Video and Audio Combiner")

# Create and pack UI elements
video_label = Label(root, text="Select a video file:")
video_label.pack(pady=10)

audio_label = Label(root, text="Select an audio file:")
audio_label.pack(pady=10)

button_video = Button(root, text="Upload Video", command=upload_video)
button_video.pack(pady=10)

button_audio = Button(root, text="Upload Audio", command=upload_audio)
button_audio.pack(pady=10)

button_combine = Button(root, text="Combine Files", command=combine_files)
button_combine.pack(pady=10)

info_label = Label(root, text="")
info_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
