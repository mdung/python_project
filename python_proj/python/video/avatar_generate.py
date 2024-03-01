import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from moviepy.editor import VideoClip, TextClip, CompositeVideoClip, ColorClip
from moviepy.video.VideoClip import ImageClip


class RandomVideoGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Random Video Generator')

        self.label = QLabel('Select an image (optional):')
        self.button_browse = QPushButton('Browse')
        self.button_browse.clicked.connect(self.browse_image)
        self.button_generate = QPushButton('Generate Random Video')
        self.button_generate.clicked.connect(self.generate_random_video)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_browse)
        layout.addWidget(self.button_generate)

        self.setLayout(layout)

    def browse_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, 'Select an image', '', 'Image Files (*.png *.jpg *.jpeg)')
        if image_path:
            self.image_path = image_path
            self.label.setText(f'Selected image: {os.path.basename(self.image_path)}')

    def generate_random_video(self):
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        text_to_speak = "This is a random video!"

        # Generate a random color video clip
        color_clip = ColorClip(size=(640, 480), color=background_color).set_duration(5)

        # Generate a text clip
        text_clip = TextClip(text_to_speak, fontsize=24, color='white', bg_color=None).set_pos('center').set_duration(5)

        # Optionally, add an image clip if selected
        if hasattr(self, 'image_path') and os.path.exists(self.image_path):
            image_clip = ImageClip(self.image_path).set_duration(5)
            video_clip = CompositeVideoClip([color_clip, image_clip, text_clip])
        else:
            video_clip = CompositeVideoClip([color_clip, text_clip])

        # Output video path
        video_output_path = os.path.join('output', 'random_video.mp4')
        video_clip.write_videofile(video_output_path, codec="libx264", audio_codec="aac", fps=24)

        self.label.setText(f'Random video generated successfully: {video_output_path}')

if __name__ == '__main__':
    app = QApplication([])
    window = RandomVideoGeneratorApp()
    window.show()
    app.exec_()
