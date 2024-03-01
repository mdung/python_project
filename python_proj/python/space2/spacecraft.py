import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class SolarFlareSimulator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Solar Flare Simulator")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.create_widgets()
        self.create_simulation_plot()

    def create_widgets(self):
        self.simulate_button = QPushButton("Simulate", self)
        self.simulate_button.clicked.connect(self.simulate)
        self.layout.addWidget(self.simulate_button)

    def create_simulation_plot(self):
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def simulate(self):
        # Add your simulation code here
        # Example: Generate random data for demonstration
        time = np.linspace(0, 10, 100)
        data = np.random.rand(100)

        # Plot the simulated data
        self.ax.clear()
        self.ax.plot(time, data)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Simulation Data")
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = SolarFlareSimulator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
