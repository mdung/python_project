from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_subtitles(video_path, subtitle_path, output_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Read subtitle file
    with open(subtitle_path, 'r', encoding='utf-8') as subtitle_file:
        subtitle_content = subtitle_file.read()

    # Extract subtitle data from SMI file
    subtitle_data = []
    lines = subtitle_content.splitlines()
    for line in lines:
        if line.startswith('<SYNC'):
            start_time = int(line.split('=')[1].split('>')[0])
        elif line.startswith('<P class'):
            subtitle_text = line.split('>', 1)[1].split('<')[0].replace('&nbsp;', ' ')
            subtitle_data.append((start_time / 1000, subtitle_text))

    # Create TextClip for each subtitle
    subtitle_clips = []
    for start_time, text in subtitle_data:
        subtitle_clip = TextClip(text, fontsize=24, color='white', bg_color='black', size=(video_clip.size[0], 50))
        subtitle_clips.append(subtitle_clip.set_position(('center', 'bottom')).set_start(start_time))

    # Overlay subtitles on the video
    video_with_subtitles = CompositeVideoClip([video_clip] + subtitle_clips)

    # Write the final video with subtitles
    print("Writing video with subtitles...")
    video_with_subtitles.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True, logger='bar')

# Replace 'video.mp4' and 'text.smi' with your actual video and subtitle file paths
add_subtitles('video.mp4', 'text.smi', 'output_video_with_subtitles.mp4')
