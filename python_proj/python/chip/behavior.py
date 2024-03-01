import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class ChipPackagingSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Chip Packaging Simulator")

        self.create_widgets()

    def create_widgets(self):
        self.parameter_label = ttk.Label(self.master, text="Simulation Parameter:")
        self.parameter_label.pack(pady=10)

        self.parameter_var = tk.DoubleVar()
        self.parameter_entry = ttk.Entry(self.master, textvariable=self.parameter_var)
        self.parameter_entry.pack(pady=10)

        self.simulate_button = ttk.Button(self.master, text="Simulate", command=self.simulate)
        self.simulate_button.pack(pady=10)

        self.plot_frame = ttk.Frame(self.master)
        self.plot_frame.pack(pady=10)

    def simulate(self):
        try:
            parameter_value = self.parameter_var.get()

            # Simulate chip packaging process (example: exponential decay)
            time_values = np.linspace(0, 10, 100)
            packaging_quality = np.exp(-parameter_value * time_values)

            # Plot the simulation result
            self.plot_simulation_result(time_values, packaging_quality)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid parameter value. Please enter a numeric value.")

    def plot_simulation_result(self, time_values, packaging_quality):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(time_values, packaging_quality, label="Packaging Quality")
        ax.set_xlabel("Time")
        ax.set_ylabel("Packaging Quality")
        ax.legend()

        # Embed the Matplotlib plot in the Tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == '__main__':
    root = tk.Tk()
    app = ChipPackagingSimulator(root)
    root.mainloop()
