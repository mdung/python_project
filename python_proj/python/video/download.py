import os
from tkinter import Tk, Label, Button, Entry, filedialog
from pytube import YouTube

def download_video():
    video_url = entry_url.get()

    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(file_extension="mp4").first()
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])

        if output_path:
            stream.download(output_path)
            info_label.config(text=f"Video downloaded successfully to:\n{output_path}")
        else:
            info_label.config(text="Download canceled.")
    except Exception as e:
        info_label.config(text=f"Error: {str(e)}")

# Create a Tkinter window
root = Tk()
root.title("YouTube Video Downloader")

# Create and pack UI elements
label_url = Label(root, text="YouTube Video URL:")
label_url.pack(pady=10)

entry_url = Entry(root, width=50)
entry_url.pack(pady=10)

button_download = Button(root, text="Download Video", command=download_video)
button_download.pack(pady=10)

info_label = Label(root, text="")
info_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
