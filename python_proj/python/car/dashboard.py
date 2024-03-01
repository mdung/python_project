import tkinter as tk
import random

class CarDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Car Dashboard")
        self.geometry("400x200")

        self.speed_label = tk.Label(self, text="Speed:")
        self.speed_label.pack(pady=10)

        self.speed_var = tk.StringVar()
        self.speed_var.set("0 km/h")
        self.speed_display = tk.Label(self, textvariable=self.speed_var, font=("Helvetica", 24))
        self.speed_display.pack()

        self.rpm_label = tk.Label(self, text="RPM:")
        self.rpm_label.pack(pady=10)

        self.rpm_var = tk.StringVar()
        self.rpm_var.set("0 RPM")
        self.rpm_display = tk.Label(self, textvariable=self.rpm_var, font=("Helvetica", 24))
        self.rpm_display.pack()

        self.update_dashboard()

    def update_dashboard(self):
        # Simulate speed and RPM data (replace with your actual data source)
        speed = random.randint(0, 120)
        rpm = random.randint(800, 6000)

        self.speed_var.set(f"{speed} km/h")
        self.rpm_var.set(f"{rpm} RPM")

        # Schedule the update every 1000 milliseconds (1 second)
        self.after(1000, self.update_dashboard)

if __name__ == "__main__":
    car_dashboard = CarDashboard()
    car_dashboard.mainloop()
