import tkinter as tk
from math import cos, sin, radians

class ParkingAssistanceSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Parking Assistance System")
        self.geometry("600x400")

        self.canvas = tk.Canvas(self, bg="white", width=600, height=400)
        self.canvas.pack()

        self.car = self.canvas.create_rectangle(50, 150, 100, 200, fill="blue")
        self.parking_space = self.canvas.create_rectangle(400, 50, 550, 200, fill="green")

        self.parking_text = tk.StringVar()
        self.parking_label = tk.Label(self, textvariable=self.parking_text, font=("Helvetica", 16))
        self.parking_label.pack(pady=10)

        self.simulate_button = tk.Button(self, text="Simulate Parking", command=self.simulate_parking)
        self.simulate_button.pack(pady=20)

    def simulate_parking(self):
        # Simulate parking maneuver
        for _ in range(40):
            self.canvas.move(self.car, 5, 0)
            self.update()
            self.after(50)

        self.parking_text.set("Parking successful!")

if __name__ == "__main__":
    parking_assistance_system = ParkingAssistanceSystem()
    parking_assistance_system.mainloop()
