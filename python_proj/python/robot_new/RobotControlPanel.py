import tkinter as tk
from tkinter import Scale

class RobotControlPanel:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Control Panel")

        # Speed control
        self.speed_label = tk.Label(master, text="Speed:")
        self.speed_label.grid(row=0, column=0, pady=10)
        self.speed_scale = Scale(master, from_=0, to=100, orient="horizontal")
        self.speed_scale.grid(row=0, column=1, pady=10)

        # Sensitivity control
        self.sensitivity_label = tk.Label(master, text="Sensitivity:")
        self.sensitivity_label.grid(row=1, column=0, pady=10)
        self.sensitivity_scale = Scale(master, from_=0, to=100, orient="horizontal")
        self.sensitivity_scale.grid(row=1, column=1, pady=10)

        # Apply button
        self.apply_button = tk.Button(master, text="Apply", command=self.apply_settings)
        self.apply_button.grid(row=2, column=0, columnspan=2, pady=10)

    def apply_settings(self):
        speed_value = self.speed_scale.get()
        sensitivity_value = self.sensitivity_scale.get()

        # You can add code here to apply the settings to your robot

        print(f"Settings Applied - Speed: {speed_value}, Sensitivity: {sensitivity_value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotControlPanel(root)
    root.mainloop()
