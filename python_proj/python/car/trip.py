import tkinter as tk
import time

class TripComputer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Virtual Trip Computer")
        self.geometry("400x200")

        self.distance_label = tk.Label(self, text="Distance Traveled:")
        self.distance_label.pack(pady=10)

        self.distance_var = tk.StringVar()
        self.distance_var.set("0.0 km")
        self.distance_display = tk.Label(self, textvariable=self.distance_var, font=("Helvetica", 18))
        self.distance_display.pack()

        self.time_label = tk.Label(self, text="Time Elapsed:")
        self.time_label.pack(pady=10)

        self.time_var = tk.StringVar()
        self.time_var.set("0:00:00")
        self.time_display = tk.Label(self, textvariable=self.time_var, font=("Helvetica", 18))
        self.time_display.pack()

        self.start_button = tk.Button(self, text="Start Trip", command=self.start_trip)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(self, text="Stop Trip", command=self.stop_trip, state=tk.DISABLED)
        self.stop_button.pack()

        self.distance_traveled = 0.0
        self.start_time = None

    def start_trip(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.update_trip_info()

    def stop_trip(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.distance_traveled += 10.0  # Simulate distance increase (replace with your actual calculation)
            self.distance_var.set(f"{self.distance_traveled:.2f} km")
            self.time_var.set(self.format_time(elapsed_time))
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_trip_info(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.distance_var.set(f"{self.distance_traveled:.2f} km")
            self.time_var.set(self.format_time(elapsed_time))
            self.after(1000, self.update_trip_info)

    def format_time(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    trip_computer = TripComputer()
    trip_computer.mainloop()
