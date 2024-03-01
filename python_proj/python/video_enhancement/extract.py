import cv2
import os

def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the frames per second (fps) of the input video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Get the frame count
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Loop through each frame and save it as an image
    for frame_number in range(frame_count):
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as an image
        frame_name = f"frame_{frame_number + 1}.jpg"
        frame_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(frame_path, frame)

    # Release the video capture object
    cap.release()

    print(f"Frames extracted successfully to {output_folder}")

# Example usage
video_path = "C:/python_proj/python/output_video/short1.mp4/1.mp4"
output_folder = "C:/python_proj/python/output_video/short1.mp4/"
extract_frames(video_path, output_folder)
