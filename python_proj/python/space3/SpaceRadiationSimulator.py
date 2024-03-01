import tkinter as tk
from tkinter import ttk
import random

class SpaceRadiationSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Radiation Simulator")

        # Simulation parameters
        self.organism_health = 100
        self.radiation_level = 0

        # GUI components
        self.health_label = ttk.Label(root, text="Organism Health:")
        self.health_label.grid(row=0, column=0, pady=10)

        self.health_progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
        self.health_progressbar.grid(row=0, column=1, pady=10)

        self.radiation_label = ttk.Label(root, text="Radiation Level:")
        self.radiation_label.grid(row=1, column=0, pady=10)

        self.radiation_progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
        self.radiation_progressbar.grid(row=1, column=1, pady=10)

        self.simulate_button = ttk.Button(root, text="Simulate", command=self.simulate)
        self.simulate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def update_progressbars(self):
        self.health_progressbar["value"] = self.organism_health
        self.radiation_progressbar["value"] = self.radiation_level

    def simulate(self):
        # Simulate radiation exposure
        radiation_exposure = random.uniform(0, 10)
        self.radiation_level += radiation_exposure

        # Simulate health degradation based on radiation
        health_loss = min(self.radiation_level / 10, 10)
        self.organism_health -= health_loss

        # Ensure health and radiation levels are within bounds
        self.organism_health = max(0, min(100, self.organism_health))
        self.radiation_level = max(0, min(100, self.radiation_level))

        # Update progress bars
        self.update_progressbars()

        # Check if organism survives or dies
        if self.organism_health <= 0:
            self.health_label.config(text="Organism Health: DEAD")
            self.simulate_button.config(state="disabled")
        else:
            self.health_label.config(text=f"Organism Health: {int(self.organism_health)}%")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceRadiationSimulator(root)
    root.mainloop()
