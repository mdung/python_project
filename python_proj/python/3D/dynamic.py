import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from IPython.display import display, clear_output

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3D Function Contour Explorer')
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.layout = QVBoxLayout(main_widget)

        # Combo box for selecting 3D functions
        self.function_combo = QComboBox(self)
        self.function_combo.addItems(['Saddle', 'Hills and Valleys', 'Custom'])
        self.function_combo.currentIndexChanged.connect(self.update_function)
        self.layout.addWidget(self.function_combo)

        # Contour plot parameter sliders
        self.label_density = QLabel('Density:', self)
        self.slider_density = QSlider(self)
        self.slider_density.setOrientation(1)  # Vertical orientation
        self.slider_density.setRange(10, 100)
        self.slider_density.setValue(50)
        self.slider_density.valueChanged.connect(self.update_function)

        self.layout.addWidget(self.label_density)
        self.layout.addWidget(self.slider_density)

        # Matplotlib 3D canvas
        self.canvas = MatplotlibCanvas(main_widget)
        self.layout.addWidget(self.canvas)

        self.show()

    def update_function(self):
        selected_function = self.function_combo.currentText()
        density = self.slider_density.value()
        self.canvas.update_contour_plot(selected_function, density)

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        super().__init__(self.fig)
        self.setParent(parent)
        self.contour_plot = None
        self.update_contour_plot('Saddle', density=50)

    def update_contour_plot(self, function_name, density):
        self.ax.clear()

        if function_name == 'Saddle':
            x = np.linspace(-2, 2, density)
            y = np.linspace(-2, 2, density)
            x, y = np.meshgrid(x, y)
            z = x**2 - y**2
            title = 'Saddle Function Contour'
        elif function_name == 'Hills and Valleys':
            x = np.linspace(-3, 3, density)
            y = np.linspace(-3, 3, density)
            x, y = np.meshgrid(x, y)
            z = np.sin(np.sqrt(x**2 + y**2))
            title = 'Hills and Valleys Contour'
        elif function_name == 'Custom':
            # Add your custom contour plot definition here
            # Example: Define a custom function contour plot
            x = np.linspace(-2, 2, density)
            y = np.linspace(-2, 2, density)
            x, y = np.meshgrid(x, y)
            z = np.cos(np.sqrt(x**2 + y**2))
            title = 'Custom Contour Plot'
        else:
            return

        self.contour_plot = self.ax.contourf(x, y, z, cmap='viridis', alpha=0.8)
        self.ax.set_title(title)

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
