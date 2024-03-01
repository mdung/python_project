import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from IPython.display import display, clear_output

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Interactive Graphical App')
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)
        canvas = MatplotlibCanvas(main_widget)
        layout.addWidget(canvas)

        self.show()

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        super().__init__(fig)
        self.setParent(parent)

        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        self.ax.plot(x, y)
        self.ax.set_title('Sin Wave')
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
