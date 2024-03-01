import tkinter as tk
from tkinter import messagebox
import math

class Satellite:
    def __init__(self, name, altitude, velocity):
        self.name = name
        self.altitude = altitude
        self.velocity = velocity

def check_collision(satellite1, satellite2):
    # Simple collision detection based on distance and altitude
    distance = math.sqrt((satellite1.altitude - satellite2.altitude) ** 2)
    return distance < 1000  # Adjust the threshold as needed

class SatelliteCollisionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Satellite Collision Detection System")

        self.satellites = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter Satellite Information:")
        self.label.pack()

        self.name_entry = tk.Entry(self.master, width=20)
        self.name_entry.pack()

        self.altitude_entry = tk.Entry(self.master, width=20)
        self.altitude_entry.pack()

        self.velocity_entry = tk.Entry(self.master, width=20)
        self.velocity_entry.pack()

        self.add_button = tk.Button(self.master, text="Add Satellite", command=self.add_satellite)
        self.add_button.pack()

        self.check_collision_button = tk.Button(self.master, text="Check Collision", command=self.check_collision)
        self.check_collision_button.pack()

    def add_satellite(self):
        name = self.name_entry.get()
        altitude = float(self.altitude_entry.get())
        velocity = float(self.velocity_entry.get())

        satellite = Satellite(name, altitude, velocity)
        self.satellites.append(satellite)

        messagebox.showinfo("Success", f"Satellite {name} added successfully!")

    def check_collision(self):
        if len(self.satellites) < 2:
            messagebox.showwarning("Warning", "Add at least two satellites before checking for collisions.")
            return

        for i in range(len(self.satellites) - 1):
            for j in range(i + 1, len(self.satellites)):
                if check_collision(self.satellites[i], self.satellites[j]):
                    messagebox.showwarning("Collision Warning", f"Collision detected between {self.satellites[i].name} and {self.satellites[j].name}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SatelliteCollisionApp(root)
    root.mainloop()
