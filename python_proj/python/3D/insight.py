import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D

class ContourPlotApp:
    def __init__(self, master):
        self.master = master
        master.title("3D Plot with Contour Lines")

        self.create_widgets()

    def create_widgets(self):
        self.fig = plt.Figure(figsize=(6, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.plot_3d_with_contour()

    def plot_3d_with_contour(self):
        # Create sample data
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))

        # Plot 3D surface
        self.ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, rstride=100, cstride=100)

        # Add contour lines
        cset = self.ax.contour(X, Y, Z, zdir='z', offset=np.min(Z), cmap='viridis')

        # Label axes
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_zlabel('Z-axis')

        # Add colorbar
        self.fig.colorbar(cset, ax=self.ax, orientation='vertical', shrink=0.5, aspect=10)

def main():
    root = tk.Tk()
    app = ContourPlotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
