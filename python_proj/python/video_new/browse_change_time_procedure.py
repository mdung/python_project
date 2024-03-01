import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import threading
import time

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

def auto_rename_loop(folder_path):
    while auto_rename_flag.is_set():
        rename_videos_in_folder(folder_path)
        time.sleep(10)  # Wait for 10 seconds before running again

def start_auto_rename():
    auto_rename_flag.set()
    threading.Thread(target=auto_rename_loop, args=(folder_path_var.get(),)).start()

def stop_auto_rename():
    auto_rename_flag.clear()

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)
        update_label()

def update_label():
    folder_path = folder_path_var.get()
    if os.path.exists(folder_path):
        label_var.set("Video files renamed successfully!")
    else:
        label_var.set("Invalid folder path. Please provide a valid path.")

# Create main window
root = tk.Tk()
root.title("Video Renamer")

# Variables
folder_path_var = tk.StringVar()
label_var = tk.StringVar()
auto_rename_flag = threading.Event()

# Widgets
browse_button = tk.Button(root, text="Browse", command=browse_folder)
start_button = tk.Button(root, text="Start Auto Rename", command=start_auto_rename)
stop_button = tk.Button(root, text="Stop Auto Rename", command=stop_auto_rename)
label = tk.Label(root, textvariable=label_var)

# Layout
browse_button.pack(pady=10)
start_button.pack(pady=10)
stop_button.pack(pady=10)
label.pack(pady=10)

# Start GUI
root.mainloop()
