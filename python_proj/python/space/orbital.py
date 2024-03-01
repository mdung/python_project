import tkinter as tk
from tkinter import ttk
from astropy import units as u
from astropy.coordinates import solar_system_ephemeris, EarthLocation, AltAz
from astropy.time import Time

class SatelliteOrbitCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Satellite Orbit Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Satellite Information Frame
        info_frame = ttk.Frame(self.master, padding="10")
        info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(info_frame, text="Satellite Information", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(info_frame, text="Satellite Name:").grid(row=1, column=0, sticky="w")
        self.satellite_name_entry = ttk.Entry(info_frame)
        self.satellite_name_entry.grid(row=1, column=1, pady=5, sticky="ew")

        ttk.Label(info_frame, text="Altitude (km):").grid(row=2, column=0, sticky="w")
        self.altitude_entry = ttk.Entry(info_frame)
        self.altitude_entry.grid(row=2, column=1, pady=5, sticky="ew")

        # Calculate Button
        ttk.Button(info_frame, text="Calculate Orbit", command=self.calculate_orbit).grid(row=3, column=0, columnspan=2, pady=10)

        # Orbit Results Frame
        result_frame = ttk.Frame(self.master, padding="10")
        result_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(result_frame, text="Orbital Parameters", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(result_frame, text="Semi-Major Axis (a):").grid(row=1, column=0, sticky="w")
        self.semi_major_axis_label = ttk.Label(result_frame, text="")
        self.semi_major_axis_label.grid(row=1, column=1, pady=5, sticky="w")

        ttk.Label(result_frame, text="Eccentricity (e):").grid(row=2, column=0, sticky="w")
        self.eccentricity_label = ttk.Label(result_frame, text="")
        self.eccentricity_label.grid(row=2, column=1, pady=5, sticky="w")

        ttk.Label(result_frame, text="Inclination (i):").grid(row=3, column=0, sticky="w")
        self.inclination_label = ttk.Label(result_frame, text="")
        self.inclination_label.grid(row=3, column=1, pady=5, sticky="w")

    def calculate_orbit(self):
        satellite_name = self.satellite_name_entry.get()
        altitude = float(self.altitude_entry.get())

        # Calculate Orbital Parameters
        semi_major_axis = (EarthLocation.from_geodetic(0, 0, 0) + AltAz(alt=altitude * u.km)).geocentrictrueecliptic.distance.to(u.km)
        eccentricity = 0.001  # Placeholder value, you need to calculate it based on your satellite's orbit
        inclination = 30.0  # Placeholder value, you need to calculate it based on your satellite's orbit

        # Update Labels
        self.semi_major_axis_label.config(text=f"{semi_major_axis:.2f} km")
        self.eccentricity_label.config(text=f"{eccentricity:.4f}")
        self.inclination_label.config(text=f"{inclination:.2f} degrees")

def main():
    root = tk.Tk()
    app = SatelliteOrbitCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
