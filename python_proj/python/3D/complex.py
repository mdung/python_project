import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

class ComplexFunctionVisualizationApp:
    def __init__(self, master):
        self.master = master
        master.title("3D Complex Function Visualization")

        self.create_widgets()

    def create_widgets(self):
        self.fig = plt.Figure(figsize=(8, 8), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.create_complex_function_visualization()

    def create_complex_function_visualization(self):
        # Generate sample data for complex function visualization
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y  # Representing complex numbers in the Z plane

        # Define a complex function (modify as needed)
        W = np.sin(Z)

        # Plot 3D complex function visualization
        self.ax.plot_surface(X, Y, np.real(W), cmap=cm.coolwarm, alpha=0.8, rstride=100, cstride=100)
        self.ax.set_xlabel('Real Axis')
        self.ax.set_ylabel('Imaginary Axis')
        self.ax.set_zlabel('Real Part of Function')

        # Add colorbar
        cbar = self.fig.colorbar(cm.ScalarMappable(cmap=cm.coolwarm), ax=self.ax, orientation='vertical', shrink=0.5)
        cbar.set_label('Magnitude of Function')

def main():
    root = tk.Tk()
    app = ComplexFunctionVisualizationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
