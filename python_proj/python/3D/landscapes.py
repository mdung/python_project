import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import noise

class LandscapeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Dynamic 3D Landscape Generator")

        self.create_widgets()

    def create_widgets(self):
        self.fig = plt.Figure(figsize=(6, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.generate_dynamic_landscape()

    def generate_dynamic_landscape(self):
        # Generate dynamic 3D landscape using noise functions
        size = 100
        scale = 20.0
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0

        world = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                world[i][j] = noise.pnoise2(i/scale,
                                            j/scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=1024,
                                            repeaty=1024,
                                            base=42)

        x = np.arange(0, size, 1)
        y = np.arange(0, size, 1)
        x, y = np.meshgrid(x, y)

        # Plot dynamic 3D landscape
        self.ax.plot_surface(x, y, world, cmap='terrain', alpha=0.8, rstride=100, cstride=100)

        # Label axes
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_zlabel('Z-axis')

def main():
    root = tk.Tk()
    app = LandscapeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
