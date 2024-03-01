from moviepy.editor import VideoClip, AudioFileClip
from tkinter import filedialog
import tkinter as tk
import os
import numpy as np

def create_video(input_audio_file, output_video_file, image_file="background_image.jpg", fps=24):
    # Load the audio file
    audio = AudioFileClip(input_audio_file)

    # Create an initial black frame for the video
    initial_frame = np.zeros((720, 1280, 3), dtype=np.uint8)  # Use your preferred resolution

    # Set the duration of the video to match the audio
    video = VideoClip(make_frame=lambda t: initial_frame, duration=audio.duration)

    # Set the background image for the video (you can customize this)
    if os.path.isfile(image_file):
        background = VideoClip(make_frame=lambda t: None, duration=audio.duration).set_audio(audio)
    else:
        # If the image file doesn't exist, create a black background
        background = VideoClip(make_frame=lambda t: initial_frame, duration=audio.duration).set_audio(audio)

    # Combine the audio with the background video
    final_video = video.set_audio(background.audio)

    # Write the final video to the output file
    final_video.write_videofile(output_video_file, codec="libx264", audio_codec="aac", fps=fps)

    print(f"Video created successfully: {output_video_file}")

def browse_audio_file():
    audio_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if audio_file_path:
        entry_var.set(audio_file_path)

def convert_to_video():
    input_audio_file = entry_var.get()

    if not os.path.isfile(input_audio_file):
        result_label_var.set("Error: The specified audio file does not exist.")
    else:
        output_video_file = os.path.splitext(os.path.basename(input_audio_file))[0] + "_output.mp4"
        create_video(input_audio_file, output_video_file)
        result_label_var.set(f"Video creation complete. Check the console for details.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Audio to Video Converter")

    # Entry widget for displaying selected audio file path
    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, width=40)
    entry.grid(row=0, column=0, padx=10, pady=10)

    # Browse button to open file dialog for audio file
    browse_button = tk.Button(root, text="Browse", command=browse_audio_file)
    browse_button.grid(row=0, column=1, padx=10, pady=10)

    # Convert button to start audio-to-video conversion
    convert_button = tk.Button(root, text="Convert", command=convert_to_video)
    convert_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Label to display conversion result
    result_label_var = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_label_var)
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()
