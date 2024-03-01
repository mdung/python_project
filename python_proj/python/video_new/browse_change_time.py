import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def rename_videos_in_folder(folder_path):
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']  # Add more video extensions if needed

    videos = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    videos = [v for v in videos if any(v.lower().endswith(ext) for ext in video_extensions)]

    videos.sort()  # Sort files to ensure sequential numbering

    for i, old_filename in enumerate(videos, start=1):
        ext = os.path.splitext(old_filename)[1]
        new_filename = f"{i}{ext}"
        old_file_path = os.path.join(folder_path, old_filename)
        new_file_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_filename} to {new_filename}")
        except Exception as e:
            print(f"Error renaming file {old_filename}: {e}")

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)
        update_label()

def update_label():
    folder_path = folder_path_var.get()
    if os.path.exists(folder_path):
        rename_videos_in_folder(folder_path)
        label_var.set("Video files renamed successfully!")
    else:
        label_var.set("Invalid folder path. Please provide a valid path.")

# Create main window
root = tk.Tk()
root.title("Video Renamer")

# Variables
folder_path_var = tk.StringVar()
label_var = tk.StringVar()

# Widgets
browse_button = tk.Button(root, text="Browse", command=browse_folder)
label = tk.Label(root, textvariable=label_var)

# Layout
browse_button.pack(pady=10)
label.pack(pady=10)

# Start GUI
root.mainloop()
