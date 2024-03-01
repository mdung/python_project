import tkinter as tk
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body, AltAz, EarthLocation
import numpy as np

class SolarSystemVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solar System Visualizer")

        self.start_date_label = tk.Label(root, text="Start Date (YYYY-MM-DD):")
        self.start_date_label.pack()

        self.start_date_entry = tk.Entry(root)
        self.start_date_entry.pack()

        self.duration_label = tk.Label(root, text="Duration (days):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()

        self.visualize_button = tk.Button(root, text="Visualize Solar System", command=self.visualize_solar_system)
        self.visualize_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.pack()

    def visualize_solar_system(self):
        start_date_str = self.start_date_entry.get()
        duration_str = self.duration_entry.get()

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            duration = int(duration_str)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date or duration format.")
            return

        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack()

        for planet_name in ["Mercury", "Venus", "Mars", "Jupiter barycenter", "Saturn barycenter", "Uranus barycenter", "Neptune barycenter"]:
            planet_position = self.calculate_planet_positions(start_date, duration, planet_name)
            ax.plot_date(planet_position.times.plot_date, planet_position.altaz.alt, label=planet_name)

        ax.set_xlabel("Date")
        ax.set_ylabel("Altitude (degrees)")
        ax.legend()
        ax.grid(True)

        canvas.draw()

    def calculate_planet_positions(self, start_date, duration, planet_name):
        observer_location = EarthLocation(lat=0, lon=0)
        times = Time(start_date) + np.linspace(0, duration, num=1000) * u.day
        with solar_system_ephemeris.set('builtin'):
            planet_position = get_body(planet_name, times, observer_location)
        planet_position_altaz = planet_position.transform_to(AltAz(obstime=times, location=observer_location))
        return planet_position_altaz

    def quit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SolarSystemVisualizerApp(root)
    root.mainloop()
