import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import serial
import threading
import time

class RobotMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Sensor Monitor")

        # Initialize serial connection (replace 'COMx' with your actual port)
        self.serial_port = serial.Serial('COMx', baudrate=9600, timeout=1)

        # Create GUI elements
        self.create_gui()

        # Initialize data variables
        self.time_data = []
        self.sensor_data = []

        # Create and start a thread for updating data
        self.update_thread = threading.Thread(target=self.update_data, daemon=True)
        self.update_thread.start()

    def create_gui(self):
        # Create and configure the main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create a figure for plotting
        self.fig = Figure(figsize=(8, 4), dpi=100)
        self.plot_area = self.fig.add_subplot(1, 1, 1)

        # Create canvas for the figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0, padx=10, pady=10)

    def update_data(self):
        while True:
            # Read data from the serial port (modify accordingly based on your data format)
            raw_data = self.serial_port.readline().decode('utf-8').strip()

            try:
                # Extract time and sensor value from the raw data (modify accordingly)
                time_stamp, sensor_value = map(float, raw_data.split(','))

                # Append data to the lists
                self.time_data.append(time_stamp)
                self.sensor_data.append(sensor_value)

                # Update the plot
                self.plot_data()

            except ValueError:
                print("Invalid data format")

            # Add a delay to control the update rate
            time.sleep(0.1)

    def plot_data(self):
        # Clear previous plot
        self.plot_area.clear()

        # Plot the data
        self.plot_area.plot(self.time_data, self.sensor_data, label="Sensor Data")

        # Set plot labels and title
        self.plot_area.set_xlabel("Time")
        self.plot_area.set_ylabel("Sensor Value")
        self.plot_area.set_title("Real-time Sensor Data")

        # Add legend
        self.plot_area.legend()

        # Update the canvas
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotMonitorApp(root)
    root.mainloop()
