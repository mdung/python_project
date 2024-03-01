import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from moviepy.editor import VideoFileClip, concatenate_videoclips

class VideoCombinationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.video_clips = []

    def init_ui(self):
        self.setWindowTitle('Video Combination App')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.upload_button = QPushButton('Upload Video', self)
        self.upload_button.clicked.connect(self.upload_video)
        self.layout.addWidget(self.upload_button)

        self.output_label = QLabel('Output: No videos selected', self)
        self.layout.addWidget(self.output_label)

        self.combine_button = QPushButton('Combine Videos', self)
        self.combine_button.clicked.connect(self.combine_videos)
        self.layout.addWidget(self.combine_button)

        self.setLayout(self.layout)

    def upload_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Upload Video", "", "Video Files (*.mp4 *.avi);;All Files (*)", options=options)

        if file_name:
            self.video_clips.append(VideoFileClip(file_name))
            self.output_label.setText(f'Output: {len(self.video_clips)} videos selected')

    def combine_videos(self):
        if self.video_clips:
            output_file = QFileDialog.getSaveFileName(self, "Save Combined Video", "", "Video Files (*.mp4 *.avi);;All Files (*)")
            if output_file[0]:
                final_clip = concatenate_videoclips(self.video_clips)
                final_clip.write_videofile(output_file[0], codec="libx264", audio_codec="aac")
                self.output_label.setText(f'Output: Video saved as {output_file[0]}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoCombinationApp()
    window.show()
    sys.exit(app.exec_())
