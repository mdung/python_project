import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D

class ParametricSurfaceApp:
    def __init__(self, master):
        self.master = master
        master.title("Parametric 3D Surface Visualization")

        self.create_widgets()

    def create_widgets(self):
        self.fig = plt.Figure(figsize=(6, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.create_parametric_surface()

    def create_parametric_surface(self):
        # Create sample parametric data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        x = 10 * np.sin(u) * np.cos(v)
        y = 10 * np.sin(u) * np.sin(v)
        z = 10 * np.cos(u)

        # Plot parametric 3D surface
        self.ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8, rstride=100, cstride=100)

        # Label axes
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_zlabel('Z-axis')

def main():
    root = tk.Tk()
    app = ParametricSurfaceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
