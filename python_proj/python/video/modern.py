import cv2
import numpy as np
from moviepy.editor import VideoFileClip, ImageSequenceClip

def apply_old_film_effect(frame):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply noise to simulate film grain
    noise = np.random.normal(0, 25, gray_frame.shape)
    noisy_frame = np.clip(gray_frame + noise, 0, 255).astype(np.uint8)

    # Apply sepia tone
    sepia_frame = cv2.cvtColor(noisy_frame, cv2.COLOR_GRAY2BGR)
    sepia_frame = cv2.transform(sepia_frame, np.array([[0.393, 0.769, 0.189],
                                                       [0.349, 0.686, 0.168],
                                                       [0.272, 0.534, 0.131]]))

    # Add scratches to simulate old film damage
    scratch_intensity = 0.01
    scratches = np.random.rand(*frame.shape[:2]) < scratch_intensity
    sepia_frame[scratches] = 0

    return sepia_frame

def process_video(input_path, output_path):
    # Open the video clip using moviepy
    video_clip = VideoFileClip(input_path)

    # Apply the old film effect to each frame
    processed_frames = [apply_old_film_effect(frame) for frame in video_clip.iter_frames()]

    # Create a new video clip with the processed frames
    processed_clip = ImageSequenceClip(processed_frames, fps=video_clip.fps)

    # Write the processed video to the output path
    processed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    input_video_path = "D:/new_video/vn.mp4/Untitled.mp4"
    output_video_path = "output_video_old_film.mp4"

    process_video(input_video_path, output_video_path)
