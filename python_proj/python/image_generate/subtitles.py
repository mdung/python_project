import sys
import os

from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
import speech_recognition as sr
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip

class SubtitleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Subtitle Generator")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.video_label = QLabel("No Video Selected")
        self.layout.addWidget(self.video_label)

        self.upload_button = QPushButton("Upload Video")
        self.upload_button.clicked.connect(self.upload_video)
        self.layout.addWidget(self.upload_button)

        self.generate_button = QPushButton("Generate Subtitles")
        self.generate_button.clicked.connect(self.generate_subtitles)
        self.layout.addWidget(self.generate_button)

        self.central_widget.setLayout(self.layout)

        self.video_path = None

    def upload_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi);;All Files (*)", options=options)

        if video_path:
            self.video_path = video_path
            self.video_label.setText(os.path.basename(video_path))

    def generate_subtitles(self):
        if not self.video_path:
            return

        # Extract audio from video
        audio_path = os.path.splitext(self.video_path)[0] + "_audio.wav"
        video_clip = VideoFileClip(self.video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_path)
        audio_clip.close()

        # Perform speech recognition on the audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            subtitles = recognizer.recognize_google(audio)

        # Display subtitles
        subtitles_label = QLabel(subtitles)
        self.layout.addWidget(subtitles_label)

        # Create an output video with subtitles
        output_path = os.path.splitext(self.video_path)[0] + "_with_subtitles.mp4"
        video_clip = video_clip.set_audio(audio_clip)
        video_clip.write_videofile(output_path, audio_codec='aac')

        # Display avatar (replace 'avatar.png' with your avatar file)
        avatar_label = QLabel()
        pixmap = QPixmap('avatar.png')
        avatar_label.setPixmap(pixmap)
        avatar_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(avatar_label)

        # Update UI with meaningful information
        self.video_label.setText(f"Subtitles generated and saved to:\n{output_path}")

        # Clean up temporary files
        os.remove(audio_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    subtitle_app = SubtitleApp()
    subtitle_app.show()
    sys.exit(app.exec_())
