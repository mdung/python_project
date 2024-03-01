import os
import tkinter as tk
from tkinter import filedialog
from deepface import DeepFace
from moviepy.editor import VideoFileClip, TextClip

def generate_avatar(input_audio_file, output_video_file):
    # Generate text from the audio using a text-to-speech API or library
    text_from_audio = "Hello, this is your AI talking avatar."

    # Generate the avatar image using DeepFace
    avatar = DeepFace.analyze(text_from_audio, actions=['generate_avatar'])

    # Create a video clip from the avatar image
    avatar_clip = VideoFileClip(avatar['response']['image'])

    # Create a text clip with the audio transcription
    txt_clip = TextClip(text_from_audio, fontsize=24, color='white', bg_color='black')

    # Overlay the text clip on the avatar clip
    result_clip = avatar_clip.set_audio(txt_clip.audio)

    # Write the final video to the output file
    result_clip.write_videofile(output_video_file, codec="libx264", audio_codec="aac", fps=24)

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
        output_video_file = os.path.splitext(os.path.basename(input_audio_file))[0] + "_avatar_video.mp4"
        generate_avatar(input_audio_file, output_video_file)
        result_label_var.set(f"Video creation complete. Check the console for details.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("AI Avatar Video Generator")

    # Entry widget for displaying selected audio file path
    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, width=40)
    entry.grid(row=0, column=0, padx=10, pady=10)

    # Browse button to open file dialog for audio file
    browse_button = tk.Button(root, text="Browse", command=browse_audio_file)
    browse_button.grid(row=0, column=1, padx=10, pady=10)

    # Generate button to start avatar video generation
    generate_button = tk.Button(root, text="Generate Avatar Video", command=convert_to_video)
    generate_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Label to display conversion result
    result_label_var = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_label_var)
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()
