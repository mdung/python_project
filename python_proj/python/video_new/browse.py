import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def get_folder_video_duration(folder_path):
    total_duration = 0
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']  # Add more video extensions if needed

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if any(filename.lower().endswith(ext) for ext in video_extensions):
                try:
                    clip = VideoFileClip(file_path)
                    total_duration += clip.duration
                except Exception as e:
                    print(f"Error reading video file {filename}: {e}")

    return total_duration

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)
        update_duration_label()

def update_duration_label():
    folder_path = folder_path_var.get()
    if os.path.exists(folder_path):
        total_duration = get_folder_video_duration(folder_path)
        total_minutes = total_duration / 60.0
        duration_label_var.set(f"The total duration of videos in {folder_path} is: {total_duration:.2f} seconds "
                               f"({total_minutes:.2f} minutes)")
        print(f"Total duration: {total_duration:.2f} seconds, {total_minutes:.2f} minutes")
    else:
        duration_label_var.set("Invalid folder path. Please provide a valid path.")

# Create main window
root = tk.Tk()
root.title("Folder Video Duration Calculator")

# Variables
folder_path_var = tk.StringVar()
duration_label_var = tk.StringVar()

# Widgets
browse_button = tk.Button(root, text="Browse", command=browse_folder)
duration_label = tk.Label(root, textvariable=duration_label_var)

# Layout
browse_button.pack(pady=10)
duration_label.pack(pady=10)

# Start GUI
root.mainloop()
