import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import display, clear_output

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3D Plot Explorer')
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.layout = QVBoxLayout(main_widget)

        # Combo box for selecting 3D functions
        self.function_combo = QComboBox(self)
        self.function_combo.addItems(['Sine Wave', 'Sphere', 'Helix', 'Custom'])
        self.function_combo.currentIndexChanged.connect(self.update_function)
        self.layout.addWidget(self.function_combo)

        # Matplotlib 3D canvas
        self.canvas = MatplotlibCanvas(main_widget)
        self.layout.addWidget(self.canvas)

        self.show()

    def update_function(self):
        selected_function = self.function_combo.currentText()
        self.canvas.update_plot(selected_function)

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        super().__init__(self.fig)
        self.setParent(parent)
        self.update_plot('Sine Wave')

    def update_plot(self, function_name):
        self.ax.clear()

        if function_name == 'Sine Wave':
            t = np.linspace(0, 10, 100)
            x = np.sin(t)
            y = np.cos(t)
            z = t
            title = 'Sine Wave in 3D'
        elif function_name == 'Sphere':
            phi = np.linspace(0, np.pi, 100)
            theta = np.linspace(0, 2 * np.pi, 100)
            phi, theta = np.meshgrid(phi, theta)
            r = 1
            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi)
            title = '3D Sphere'
        elif function_name == 'Helix':
            t = np.linspace(0, 10, 100)
            x = np.cos(t)
            y = np.sin(t)
            z = t
            title = 'Helix in 3D'
        elif function_name == 'Custom':
            t = np.linspace(0, 10, 100)
            x = np.cos(t)
            y = np.sin(t)
            z = t**2
            title = 'Custom 3D Plot (t^2)'
        else:
            return

        self.ax.plot3D(x, y, z)
        self.ax.set_title(title)

        # Enable 3D rotation and zoom
        self.ax.view_init(elev=20, azim=30)  # Initial view angle
        self.ax.dist = 10  # Initial zoom level

        self.draw()

        # Update Jupyter output
        self.update_jupyter_output()

    def update_jupyter_output(self):
        display(plt.gcf())
        clear_output(wait=True)

if __name__ == '__main__':
    if 'ipykernel' in sys.modules:
        # Running in Jupyter Notebook, create and display the app
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        window = MyApp()
        sys.exit(app.exec_())
    else:
        # Running as a standalone application
        app = QApplication(sys.argv)
        window = MyApp()
        sys.exit(app.exec_())
