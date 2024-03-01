import os
from tkinter import Tk, Label, Button, Entry, filedialog
from tiktokapi import TikTokApi

def download_video():
    video_url = entry_url.get()

    try:
        api = TikTokApi()
        tiktok = api.get_video_by_url(video_url)

        video_bytes = tiktok['video']['downloadAddr'].content

        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])

        if output_path:
            with open(output_path, 'wb') as output_file:
                output_file.write(video_bytes)

            info_label.config(text=f"Video downloaded successfully to:\n{output_path}")
        else:
            info_label.config(text="Download canceled.")
    except Exception as e:
        info_label.config(text=f"Error: {str(e)}")

# Create a Tkinter window
root = Tk()
root.title("TikTok Video Downloader")

# Create and pack UI elements
label_url = Label(root, text="TikTok Video URL:")
label_url.pack(pady=10)

entry_url = Entry(root, width=50)
entry_url.pack(pady=10)

button_download = Button(root, text="Download Video", command=download_video)
button_download.pack(pady=10)

info_label = Label(root, text="")
info_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
