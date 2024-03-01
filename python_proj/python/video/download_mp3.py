import os
from tkinter import Tk, Label, Button, Entry, filedialog
from pytube import YouTube

def download_audio():
    video_url = entry_url.get()

    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

        if output_path:
            audio_stream.download(output_path)
            info_label.config(text=f"Audio downloaded successfully to:\n{output_path}")
        else:
            info_label.config(text="Download canceled.")
    except Exception as e:
        info_label.config(text=f"Error: {str(e)}")

# Create a Tkinter window
root = Tk()
root.title("YouTube Audio Downloader")

# Create and pack UI elements
label_url = Label(root, text="YouTube Video URL:")
label_url.pack(pady=10)

entry_url = Entry(root, width=50)
entry_url.pack(pady=10)

button_download = Button(root, text="Download Audio", command=download_audio)
button_download.pack(pady=10)

info_label = Label(root, text="")
info_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
