import tkinter as tk

class CarDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Car Dashboard")
        self.geometry("600x400")

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

        self.accelerator_button = tk.Button(self, text="Accelerate", command=self.accelerate)
        self.accelerator_button.pack(pady=20)

        self.brake_button = tk.Button(self, text="Brake", command=self.brake)
        self.brake_button.pack()

    def accelerate(self):
        # Increase speed and update the display
        current_speed = int(self.speed_var.get().split()[0])
        new_speed = current_speed + 10
        self.speed_var.set(f"{new_speed} km/h")

        # Simulate RPM increase
        current_rpm = int(self.rpm_var.get().split()[0])
        new_rpm = current_rpm + 1000
        self.rpm_var.set(f"{new_rpm} RPM")

    def brake(self):
        # Decrease speed and update the display
        current_speed = int(self.speed_var.get().split()[0])
        new_speed = max(0, current_speed - 10)
        self.speed_var.set(f"{new_speed} km/h")

        # Simulate RPM decrease
        current_rpm = int(self.rpm_var.get().split()[0])
        new_rpm = max(0, current_rpm - 1000)
        self.rpm_var.set(f"{new_rpm} RPM")

if __name__ == "__main__":
    car_dashboard = CarDashboard()
    car_dashboard.mainloop()
