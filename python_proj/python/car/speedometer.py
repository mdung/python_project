import tkinter as tk
import math

class Speedometer(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=200, height=200, bg="white")

        self.speed_label = tk.Label(self, text="Speedometer", font=("Helvetica", 12))
        self.speed_label.place(relx=0.5, rely=0.9, anchor="center")

        self.speed = 0

        self.draw_speedometer()

    def draw_speedometer(self):
        # Draw speedometer background
        self.create_oval(10, 10, 190, 190, outline="black", width=2)

        # Draw speedometer needle
        angle = math.radians(180 - self.speed * 1.8)
        x1, y1 = 100, 100
        x2, y2 = 100 + 80 * math.cos(angle), 100 - 80 * math.sin(angle)
        self.create_line(x1, y1, x2, y2, width=2, arrow=tk.LAST, arrowshape=(12, 15, 5))

    def set_speed(self, speed):
        self.speed = speed
        self.delete("all")  # Clear the canvas
        self.draw_speedometer()

class CarDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Car Dashboard")
        self.geometry("600x400")

        self.speedometer = Speedometer(self)
        self.speedometer.pack(pady=10)

        self.speed_label = tk.Label(self, text="Speed:")
        self.speed_label.pack(pady=10)

        self.speed_var = tk.StringVar()
        self.speed_var.set("0 km/h")
        self.speed_display = tk.Label(self, textvariable=self.speed_var, font=("Helvetica", 24))
        self.speed_display.pack()

        self.accelerator_button = tk.Button(self, text="Accelerate", command=self.accelerate)
        self.accelerator_button.pack(pady=20)

    def accelerate(self):
        # Increase speed and update the display
        current_speed = int(self.speed_var.get().split()[0])
        new_speed = current_speed + 10
        self.speed_var.set(f"{new_speed} km/h")
        self.speedometer.set_speed(new_speed)

if __name__ == "__main__":
    car_dashboard = CarDashboard()
    car_dashboard.mainloop()
