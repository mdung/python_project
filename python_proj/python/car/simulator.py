import tkinter as tk

class CarSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Virtual Car Simulator")
        self.geometry("600x400")

        self.speed_label = tk.Label(self, text="Speed:")
        self.speed_label.pack(pady=10)

        self.speed_var = tk.StringVar()
        self.speed_var.set("0 km/h")
        self.speed_display = tk.Label(self, textvariable=self.speed_var, font=("Helvetica", 24))
        self.speed_display.pack()

        self.steering_label = tk.Label(self, text="Steering Angle:")
        self.steering_label.pack(pady=10)

        self.steering_var = tk.StringVar()
        self.steering_var.set("0 degrees")
        self.steering_display = tk.Label(self, textvariable=self.steering_var, font=("Helvetica", 18))
        self.steering_display.pack()

        self.accelerator_button = tk.Button(self, text="Accelerate", command=self.accelerate)
        self.accelerator_button.pack(pady=10)

        self.brake_button = tk.Button(self, text="Brake", command=self.brake)
        self.brake_button.pack(pady=10)

        self.left_button = tk.Button(self, text="Turn Left", command=self.turn_left)
        self.left_button.pack(side=tk.LEFT, padx=10)

        self.right_button = tk.Button(self, text="Turn Right", command=self.turn_right)
        self.right_button.pack(side=tk.RIGHT, padx=10)

        self.speed = 0
        self.steering_angle = 0

    def accelerate(self):
        # Increase speed and update the display
        self.speed += 10
        self.speed_var.set(f"{self.speed} km/h")

    def brake(self):
        # Decrease speed and update the display
        self.speed = max(0, self.speed - 10)
        self.speed_var.set(f"{self.speed} km/h")

    def turn_left(self):
        # Turn left and update the display
        self.steering_angle = max(-45, self.steering_angle - 10)
        self.steering_var.set(f"{self.steering_angle} degrees")

    def turn_right(self):
        # Turn right and update the display
        self.steering_angle = min(45, self.steering_angle + 10)
        self.steering_var.set(f"{self.steering_angle} degrees")

if __name__ == "__main__":
    car_simulator = CarSimulator()
    car_simulator.mainloop()
