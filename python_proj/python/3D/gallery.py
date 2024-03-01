import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from IPython.display import display, clear_output

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Math Function Explorer')
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.layout = QVBoxLayout(main_widget)

        # Combo box for selecting mathematical functions
        self.function_combo = QComboBox(self)
        self.function_combo.addItems(['Sine', 'Cosine', 'Exponential', 'Custom'])
        self.function_combo.currentIndexChanged.connect(self.update_function)
        self.layout.addWidget(self.function_combo)

        # Matplotlib canvas
        self.canvas = MatplotlibCanvas(main_widget)
        self.layout.addWidget(self.canvas)

        self.show()

    def update_function(self):
        selected_function = self.function_combo.currentText()
        self.canvas.update_plot(selected_function)

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        super().__init__(fig)
        self.setParent(parent)
        self.update_plot('Sine')

    def update_plot(self, function_name):
        self.ax.clear()

        if function_name == 'Sine':
            x = np.linspace(0, 2 * np.pi, 100)
            y = np.sin(x)
            title = 'Sine Function'
        elif function_name == 'Cosine':
            x = np.linspace(0, 2 * np.pi, 100)
            y = np.cos(x)
            title = 'Cosine Function'
        elif function_name == 'Exponential':
            x = np.linspace(0, 2, 100)
            y = np.exp(x)
            title = 'Exponential Function'
        elif function_name == 'Custom':
            x = np.linspace(-2, 2, 100)
            y = x**2
            title = 'Custom Function (x^2)'
        else:
            return

        self.ax.plot(x, y)
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
