import os
from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from moviepy.editor import TextClip

# Import the DeepFace module for face analysis
from deepface import DeepFace

class AvatarGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Avatar Generator')

        self.label = QLabel('Select a photo:')
        self.button_browse = QPushButton('Browse')
        self.button_browse.clicked.connect(self.browse_photo)
        self.button_generate = QPushButton('Generate Avatar')
        self.button_generate.clicked.connect(self.generate_avatar)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_browse)
        layout.addWidget(self.button_generate)

        self.setLayout(layout)

    def browse_photo(self):
        # Use QFileDialog to select an image file
        photo_path, _ = QFileDialog.getOpenFileName(self, 'Select a photo', '', 'Image Files (*.png *.jpg *.jpeg)')
        if photo_path:
            self.photo_path = photo_path
            self.label.setText(f'Selected photo: {os.path.basename(self.photo_path)}')

    def generate_avatar(self):
        if not hasattr(self, 'photo_path'):
            self.label.setText('Error: Please select a photo first.')
            return

        # Perform face analysis with DeepFace
        try:
            result = DeepFace.analyze(self.photo_path, actions=['region'])
        except Exception as e:
            self.label.setText(f'Error analyzing photo: {str(e)}')
            return

        # Extract face embeddings from the first face analysis
        if result and 'region' in result and 'region_embedding' in result['region'][0]:
            face_embedding = result['region'][0]['region_embedding']
        else:
            self.label.setText('Error: Could not find face in the photo.')
            return

        # Generate text for TTS
        text_to_speak = "Hello, this is your AI talking avatar."

        # Generate audio using gTTS
        tts = gTTS(text=text_to_speak, lang='en', slow=False)
        audio_output_path = 'output/audio_output.mp3'
        tts.save(audio_output_path)

        # Generate video using MoviePy
        avatar_clip = TextClip(text_to_speak, fontsize=24, color='white', bg_color='black', size=(640, 480))
        avatar_clip = avatar_clip.set_audio(avatar_clip.audio.set_duration(tts.duration))
        video_output_path = 'output/avatar_video.mp4'
        avatar_clip.write_videofile(video_output_path, codec="libx264", audio_codec="aac", fps=24)

        self.label.setText('Avatar generated successfully.')

if __name__ == '__main__':
    app = QApplication([])
    window = AvatarGeneratorApp()
    window.show()
    app.exec_()
