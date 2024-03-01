import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

# Create a directory to store frames
output_directory = "video_frames"
os.makedirs(output_directory, exist_ok=True)

# Create a Tkinter window (it won't be shown)
root = Tk()
root.withdraw()

# Ask the user to select an image file
avatar_path = filedialog.askopenfilename(title="Select Avatar Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

if not avatar_path:
    print("No file selected. Exiting.")
    exit()

# Load avatar image
avatar = cv2.imread(avatar_path, cv2.IMREAD_UNCHANGED)
avatar = cv2.resize(avatar, (100, 100))  # Resize the avatar to fit the specified region
avatar_height, avatar_width, _ = avatar.shape

# Function to generate frames
def generate_frame(frame_number):
    # Example: Create a gradient as a simple frame
    height, width = 480, 640
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:, :] = [frame_number % 256, 255, 128]

    # Overlay the resized avatar onto the frame
    frame[50:50 + avatar_height, 50:50 + avatar_width] = avatar[:, :, :3]  # Assuming the avatar has an alpha channel

    return frame

# Video settings
fps = 30
duration_seconds = 10
output_file = "output_video.mp4"

# OpenCV VideoWriter settings
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_file, fourcc, fps, (640, 480))

# Generate frames and save them
for frame_number in range(int(fps * duration_seconds)):
    frame = generate_frame(frame_number)

    # Save the frame with a meaningful name
    frame_name = os.path.join(output_directory, f"frame_{frame_number:04d}.png")
    cv2.imwrite(frame_name, frame)

    # Write the frame to the video
    video_writer.write(frame)

# Release the VideoWriter
video_writer.release()

print(f"Video generated and saved as {output_file}")
