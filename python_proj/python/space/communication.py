import tkinter as tk
from datetime import datetime, timedelta
from tokenize import u

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from astropy.coordinates import EarthLocation, AltAz, get_sun, get_moon
from astropy.time import Time
import numpy as np

class SatelliteCommunicationSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Satellite Communication Simulator")

        self.start_time_label = tk.Label(root, text="Start Time (YYYY-MM-DD HH:mm:ss):")
        self.start_time_label.pack()

        self.start_time_entry = tk.Entry(root)
        self.start_time_entry.pack()

        self.duration_label = tk.Label(root, text="Duration (minutes):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()

        self.visualize_button = tk.Button(root, text="Visualize Communication", command=self.visualize_communication)
        self.visualize_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.pack()

    def visualize_communication(self):
        start_time_str = self.start_time_entry.get()
        duration_str = self.duration_entry.get()

        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
            duration = int(duration_str)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date or duration format.")
            return

        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack()

        observer_location = EarthLocation(lat=0, lon=0)
        times = Time(start_time) + np.linspace(0, duration, num=1000) * u.minute

        # Satellite orbit simulation (for illustration purposes)
        satellite_altaz = AltAz(alt=90 * u.deg, az=0 * u.deg, obstime=times, location=observer_location)
        satellite_positions = satellite_altaz.transform_to(AltAz(obstime=times, location=observer_location))

        # Sun and Moon position simulation (for illustration purposes)
        sun_positions = get_sun(times).transform_to(AltAz(obstime=times, location=observer_location))
        moon_positions = get_moon(times).transform_to(AltAz(obstime=times, location=observer_location))

        ax.plot_date(times.plot_date, satellite_positions.alt, label="Satellite", linestyle='-', marker='None')
        ax.plot_date(times.plot_date, sun_positions.alt, label="Sun", linestyle='-', marker='None')
        ax.plot_date(times.plot_date, moon_positions.alt, label="Moon", linestyle='-', marker='None')

        ax.set_xlabel("Time")
        ax.set_ylabel("Altitude (degrees)")
        ax.legend()
        ax.grid(True)

        canvas.draw()

    def quit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SatelliteCommunicationSimulatorApp(root)
    root.mainloop()
