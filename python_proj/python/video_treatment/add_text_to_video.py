import cv2
import numpy as np
from PIL import Image, ImageDraw
from moviepy.editor import VideoFileClip, ImageSequenceClip

def add_text_to_video(video_path, text, output_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Get video properties
    width, height = int(video_clip.size[0]), int(video_clip.size[1])
    fps = video_clip.fps

    # Create a list to store modified frames
    frames_with_text = []

    # Iterate through video frames
    for frame in video_clip.iter_frames(fps=fps, dtype='uint8'):
        # Convert the NumPy array to an image
        img = Image.fromarray(frame)

        # Add text to the image using Pillow
        draw = ImageDraw.Draw(img)
        draw.text((width//4, height//4), text, fill=(255, 255, 255), font=None)  # Adjust position and font as needed

        # Convert the image back to a NumPy array
        frame_with_text = np.array(img)

        # Append the frame with text to the list
        frames_with_text.append(frame_with_text)

    # Create a new VideoClip from the modified frames
    video_with_text = ImageSequenceClip(frames_with_text, fps=fps)

    # Set the duration and audio for the new video
    video_with_text = video_with_text.set_duration(video_clip.duration)
    video_with_text = video_with_text.set_audio(video_clip.audio)

    # Write the final video with text
    video_with_text.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

# Replace 'video.mp4', 'Hello world', and 'output_video_with_text.mp4'
# with your actual video file, desired text, and output file paths
add_text_to_video('video.mp4', 'Hello world', 'output_video_with_text.mp4')
