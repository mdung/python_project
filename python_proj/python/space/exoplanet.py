import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExoplanetDataGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exoplanet Data Generator and Habitable Zones")

        self.num_planets_label = ttk.Label(root, text="Number of Exoplanets:")
        self.num_planets_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.num_planets_entry = ttk.Entry(root)
        self.num_planets_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate Data", command=self.generate_exoplanet_data)
        self.generate_button.grid(row=0, column=2, padx=10, pady=10)

        self.plot_button = ttk.Button(root, text="Plot Habitable Zones", command=self.plot_habitable_zones)
        self.plot_button.grid(row=0, column=3, padx=10, pady=10)

        self.quit_button = ttk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.grid(row=0, column=4, padx=10, pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        self.exoplanet_data = None

    def generate_exoplanet_data(self):
        try:
            num_planets = int(self.num_planets_entry.get())
            self.exoplanet_data = self.generate_random_exoplanet_data(num_planets)
            tk.messagebox.showinfo("Success", "Exoplanet data generated successfully.")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid number of exoplanets. Please enter a valid integer.")

    def generate_random_exoplanet_data(self, num_planets):
        np.random.seed(42)

        planet_names = [f"Exoplanet {i+1}" for i in range(num_planets)]
        orbital_distances = np.random.uniform(0.1, 2, num_planets)  # Example range, in AU (astronomical units)
        stellar_luminosities = np.random.uniform(0.5, 2, num_planets)  # Example range, relative to the Sun

        exoplanet_data = {
            "PlanetName": planet_names,
            "OrbitalDistanceAU": orbital_distances,
            "StellarLuminosityRelative": stellar_luminosities,
        }

        return exoplanet_data

    def plot_habitable_zones(self):
        if self.exoplanet_data is None:
            tk.messagebox.showwarning("Warning", "Please generate exoplanet data first.")
            return

        self.ax.clear()

        orbital_distances = self.exoplanet_data["OrbitalDistanceAU"]
        stellar_luminosities = self.exoplanet_data["StellarLuminosityRelative"]

        habitable_zones = self.calculate_habitable_zones(orbital_distances, stellar_luminosities)

        self.ax.scatter(orbital_distances, stellar_luminosities, label="Exoplanets")
        self.ax.fill_between(habitable_zones, 0, 3, color='green', alpha=0.3, label="Habitable Zone")

        self.ax.set_xlabel("Orbital Distance (AU)")
        self.ax.set_ylabel("Stellar Luminosity (Relative to the Sun)")
        self.ax.set_title("Exoplanet Data and Habitable Zones")

        self.ax.legend()
        self.ax.grid(True)

        self.canvas.draw()

    def calculate_habitable_zones(self, orbital_distances, stellar_luminosities):
        # Example calculation for habitable zone
        habitable_zones = np.sqrt(stellar_luminosities / 1.1) * orbital_distances
        return habitable_zones

    def quit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExoplanetDataGeneratorApp(root)
    root.mainloop()
