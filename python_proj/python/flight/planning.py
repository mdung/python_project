import tkinter as tk
from tkinter import ttk

class FlightPlanningTool:
    def __init__(self, master):
        self.master = master
        master.title("Flight Planning Tool")

        # Variables for user input
        self.waypoints_var = tk.StringVar()
        self.selected_aircraft_var = tk.StringVar(value="Fighter Jet")  # Default aircraft type

        # Aircraft parameters
        self.aircraft_parameters = {
            "Fighter Jet": {"speed": 500, "fuel_consumption": 50},
            "Passenger Plane": {"speed": 300, "fuel_consumption": 30},
        }

        self.create_widgets()

    def create_widgets(self):
        # Waypoints Input
        waypoints_label = ttk.Label(self.master, text="Waypoints (comma-separated):")
        waypoints_entry = ttk.Entry(self.master, textvariable=self.waypoints_var)

        # Aircraft Type Selection
        aircraft_label = ttk.Label(self.master, text="Select Aircraft Type:")
        aircraft_combobox = ttk.Combobox(self.master, textvariable=self.selected_aircraft_var,
                                         values=list(self.aircraft_parameters.keys()))

        # Flight Planning Button
        plan_flight_button = ttk.Button(self.master, text="Plan Flight", command=self.plan_flight)

        # Layout
        waypoints_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        waypoints_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        aircraft_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        aircraft_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        plan_flight_button.grid(row=2, column=0, columnspan=2, pady=10)

    def plan_flight(self):
        waypoints = self.waypoints_var.get().split(',')
        aircraft_type = self.selected_aircraft_var.get()

        if not waypoints or not aircraft_type:
            tk.messagebox.showerror("Error", "Please enter waypoints and select an aircraft type.")
            return

        aircraft_speed = self.aircraft_parameters[aircraft_type]["speed"]
        fuel_consumption_rate = self.aircraft_parameters[aircraft_type]["fuel_consumption"]

        total_distance = 0
        for i in range(1, len(waypoints)):
            total_distance += self.calculate_distance(waypoints[i - 1], waypoints[i])

        flight_time = total_distance / aircraft_speed
        fuel_consumed = flight_time * fuel_consumption_rate

        # Display Flight Plan
        flight_plan_message = f"Flight Plan for {aircraft_type}:\n\n"
        flight_plan_message += f"Waypoints: {waypoints}\n"
        flight_plan_message += f"Total Distance: {total_distance:.2f} km\n"
        flight_plan_message += f"Flight Time: {flight_time:.2f} hours\n"
        flight_plan_message += f"Fuel Consumed: {fuel_consumed:.2f} units"

        tk.messagebox.showinfo("Flight Plan", flight_plan_message)

    def calculate_distance(self, point1, point2):
        # Simplified distance calculation (assuming flat Earth)
        return 100 * abs(ord(point1[0]) - ord(point2[0]))

if __name__ == '__main__':
    root = tk.Tk()
    app = FlightPlanningTool(root)
    root.mainloop()
