import os
import subprocess

def download_youtube_video(video_url, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Build the command to download the video using youtube-dl
    command = f"youtube-dl -o '{output_folder}/%(title)s.%(ext)s' {video_url}"

    # Run the command using subprocess
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Specify the YouTube video URL and output folder
    video_url = "https://www.youtube.com/watch?v=wSRj_qVzTAU"
    output_folder = "D:\youtube"

    # Call the download_youtube_video function
    download_youtube_video(video_url, output_folder)
