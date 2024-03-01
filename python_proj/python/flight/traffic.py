import tkinter as tk
from tkinter import ttk
import random

class Aircraft:
    def __init__(self, callsign, altitude, heading):
        self.callsign = callsign
        self.altitude = altitude
        self.heading = heading

class AirTrafficControl(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Air Traffic Control Simulator")
        self.geometry("800x600")

        self.aircraft_list = []
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=600, height=500, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

        self.add_aircraft_button = ttk.Button(self, text="Add Aircraft", command=self.add_aircraft)
        self.add_aircraft_button.grid(row=0, column=1, padx=10, pady=10)

        self.remove_aircraft_button = ttk.Button(self, text="Remove Aircraft", command=self.remove_aircraft)
        self.remove_aircraft_button.grid(row=1, column=1, padx=10, pady=10)

        self.control_frame = ttk.Frame(self)
        self.control_frame.grid(row=2, column=1, padx=10, pady=10)

        self.heading_label = ttk.Label(self.control_frame, text="Heading:")
        self.heading_label.grid(row=0, column=0, padx=5, pady=5)

        self.heading_entry = ttk.Entry(self.control_frame)
        self.heading_entry.grid(row=0, column=1, padx=5, pady=5)

        self.altitude_label = ttk.Label(self.control_frame, text="Altitude:")
        self.altitude_label.grid(row=1, column=0, padx=5, pady=5)

        self.altitude_entry = ttk.Entry(self.control_frame)
        self.altitude_entry.grid(row=1, column=1, padx=5, pady=5)

        self.communicate_button = ttk.Button(self.control_frame, text="Communicate", command=self.communicate)
        self.communicate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_aircraft(self):
        callsign = f"A{len(self.aircraft_list) + 1}"
        altitude = random.randint(10000, 30000)
        heading = random.randint(0, 360)

        aircraft = Aircraft(callsign, altitude, heading)
        self.aircraft_list.append(aircraft)

        self.update_canvas()

    def remove_aircraft(self):
        if self.aircraft_list:
            removed_aircraft = self.aircraft_list.pop()
            print(f"Removed Aircraft {removed_aircraft.callsign}")

            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")

        for aircraft in self.aircraft_list:
            x, y = self.calculate_position(aircraft.altitude, aircraft.heading)
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
            self.canvas.create_text(x, y, text=aircraft.callsign, fill="white")

    def calculate_position(self, altitude, heading):
        x = 300 + 2 * altitude * tk.math.sin(tk.math.radians(heading))
        y = 250 - 2 * altitude * tk.math.cos(tk.math.radians(heading))
        return x, y

    def communicate(self):
        selected_aircraft = self.aircraft_list[-1] if self.aircraft_list else None

        if selected_aircraft:
            new_heading = int(self.heading_entry.get())
            new_altitude = int(self.altitude_entry.get())

            selected_aircraft.heading = new_heading
            selected_aircraft.altitude = new_altitude

            print(f"Communicated new heading {new_heading} and altitude {new_altitude} to {selected_aircraft.callsign}")

            self.update_canvas()

if __name__ == "__main__":
    app = AirTrafficControl()
    app.mainloop()
