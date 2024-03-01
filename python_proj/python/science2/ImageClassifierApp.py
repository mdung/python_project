import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

class ImageClassifierApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Classifier')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.load_button = QPushButton('Load Image', self)
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        self.predict_button = QPushButton('Predict', self)
        self.predict_button.clicked.connect(self.predict_image)
        self.layout.addWidget(self.predict_button)

        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

        self.model = self.load_model()

    def load_model(self):
        # Load your trained model here
        # Replace 'path_to_your_model.h5' with the actual path to your trained model file
        model_path = 'path_to_your_model.h5'
        model = tf.keras.models.load_model(model_path)
        return model

    def load_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp *.tif *.tiff);;All Files (*)", options=options)

        if image_path:
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaledToWidth(400, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap)
            self.image_path = image_path

    def preprocess_image(self):
        if hasattr(self, 'image_path'):
            img = image.load_img(self.image_path, target_size=(224, 224))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            return img_array
        else:
            return None

    def predict_image(self):
        img_array = self.preprocess_image()

        if img_array is not None:
            # Normalize the image array
            img_array /= 255.0

            # Make prediction
            predictions = self.model.predict(img_array)

            # Display the prediction result
            class_names = ['Class1', 'Class2', 'Class3']  # Replace with your actual class names
            predicted_class = class_names[np.argmax(predictions)]

            result_text = f"Predicted Class: {predicted_class}"
            self.result_label.setText(result_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ImageClassifierApp()
    mainWindow.show()
    sys.exit(app.exec_())
