import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Hohmann transfer orbit calculation function
def hohmann_transfer(orbit1_radius, orbit2_radius):
    semi_major_axis1 = orbit1_radius
    semi_major_axis2 = orbit2_radius

    transfer_orbit_radius = (semi_major_axis1 + semi_major_axis2) / 2
    delta_v1 = np.sqrt(2 * semi_major_axis2 / (semi_major_axis1 + semi_major_axis2)) - 1
    delta_v2 = 1 - np.sqrt(2 * semi_major_axis1 / (semi_major_axis1 + semi_major_axis2))

    return transfer_orbit_radius, delta_v1, delta_v2

# Function to update the plot based on user input
def update_plot():
    orbit1_radius = float(entry_orbit1.get())
    orbit2_radius = float(entry_orbit2.get())

    transfer_orbit_radius, delta_v1, delta_v2 = hohmann_transfer(orbit1_radius, orbit2_radius)

    # Update the plot
    ax.clear()
    ax.set_title("Hohmann Transfer Orbit")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Plotting orbits
    orbit1_circle = plt.Circle((0, 0), orbit1_radius, color='b', fill=False, linestyle='dashed')
    orbit2_circle = plt.Circle((0, 0), orbit2_radius, color='r', fill=False, linestyle='dashed')
    transfer_orbit_circle = plt.Circle((0, 0), transfer_orbit_radius, color='g', fill=False)

    ax.add_patch(orbit1_circle)
    ax.add_patch(orbit2_circle)
    ax.add_patch(transfer_orbit_circle)

    # Display delta-v values
    delta_v_text = f"Delta-v1: {delta_v1:.4f}\nDelta-v2: {delta_v2:.4f}"
    ax.text(0, 0, delta_v_text, horizontalalignment='center', verticalalignment='center', fontsize=10)

    canvas.draw()

# GUI setup
root = tk.Tk()
root.title("Hohmann Transfer Orbit Calculator")

# Frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and entry widgets
ttk.Label(frame, text="Orbit 1 Radius:").grid(row=0, column=0, sticky=tk.W)
entry_orbit1 = ttk.Entry(frame)
entry_orbit1.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame, text="Orbit 2 Radius:").grid(row=1, column=0, sticky=tk.W)
entry_orbit2 = ttk.Entry(frame)
entry_orbit2.grid(row=1, column=1, sticky=tk.W)

# Button to calculate and update plot
calculate_button = ttk.Button(frame, text="Calculate", command=update_plot)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Matplotlib figure and canvas
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Run the GUI
root.mainloop()
