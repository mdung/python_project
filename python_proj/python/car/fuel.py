import tkinter as tk
import math

class FuelGauge(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=200, height=200, bg="white")

        self.fuel_label = tk.Label(self, text="Fuel Gauge", font=("Helvetica", 12))
        self.fuel_label.place(relx=0.5, rely=0.9, anchor="center")

        self.fuel_level = 0

        self.draw_fuel_gauge()

    def draw_fuel_gauge(self):
        # Draw fuel gauge background
        self.create_oval(10, 10, 190, 190, outline="black", width=2)

        # Draw fuel gauge indicator
        angle = math.radians(180 - self.fuel_level * 1.8)
        x1, y1 = 100, 100
        x2, y2 = 100 + 80 * math.cos(angle), 100 - 80 * math.sin(angle)
        self.create_line(x1, y1, x2, y2, width=4, fill="green")

    def set_fuel_level(self, fuel_level):
        self.fuel_level = fuel_level
        self.delete("all")  # Clear the canvas
        self.draw_fuel_gauge()

class CarDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Car Dashboard")
        self.geometry("600x400")

        self.fuel_gauge = FuelGauge(self)
        self.fuel_gauge.pack(pady=10)

        self.fuel_label = tk.Label(self, text="Fuel Level:")
        self.fuel_label.pack(pady=10)

        self.fuel_var = tk.StringVar()
        self.fuel_var.set("50%")
        self.fuel_display = tk.Label(self, textvariable=self.fuel_var, font=("Helvetica", 24))
        self.fuel_display.pack()

        self.consume_button = tk.Button(self, text="Consume Fuel", command=self.consume_fuel)
        self.consume_button.pack(pady=20)

    def consume_fuel(self):
        # Decrease fuel level and update the display
        current_fuel = int(self.fuel_var.get().split("%")[0])
        new_fuel = max(0, current_fuel - 10)
        self.fuel_var.set(f"{new_fuel}%")
        self.fuel_gauge.set_fuel_level(new_fuel)

if __name__ == "__main__":
    car_dashboard = CarDashboard()
    car_dashboard.mainloop()
