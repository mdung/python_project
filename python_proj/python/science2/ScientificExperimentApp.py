import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QFileDialog, QWidget
from PyQt5.QtCore import Qt


class ScientificExperimentApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scientific Experiment Analyzer')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.data_label = QLabel(self)
        self.data_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.data_label)

        self.load_button = QPushButton('Load Data', self)
        self.load_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.load_button)

        self.analyze_button = QPushButton('Analyze and Visualize', self)
        self.analyze_button.clicked.connect(self.analyze_and_visualize)
        self.layout.addWidget(self.analyze_button)

        self.central_widget.setLayout(self.layout)

        self.data = None

    def load_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        data_path, _ = QFileDialog.getOpenFileName(self, "Open Data File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if data_path:
            with open(data_path, 'r') as file:
                # Assuming the data is in a simple text file with one column of numerical values
                self.data = np.loadtxt(file)

            self.data_label.setText(f"Data loaded from {data_path}")

    def analyze_and_visualize(self):
        if self.data is not None:
            # Perform data analysis (replace with your actual analysis)
            mean_value = np.mean(self.data)
            std_dev = np.std(self.data)

            # Visualize the data (replace with your actual visualization)
            plt.figure()
            plt.hist(self.data, bins=20, color='blue', edgecolor='black')
            plt.title('Histogram of Experiment Data')
            plt.xlabel('Values')
            plt.ylabel('Frequency')

            # Display the analysis results
            result_text = f"Mean: {mean_value:.2f}, Standard Deviation: {std_dev:.2f}"
            plt.figtext(0.5, 0.02, result_text, ha='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

            plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ScientificExperimentApp()
    mainWindow.show()
    sys.exit(app.exec_())
