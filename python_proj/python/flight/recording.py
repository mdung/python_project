import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

class FlightRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flight Recorder")

        # Create widgets
        self.record_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.playback_button = tk.Button(master, text="Playback", command=self.playback)
        self.canvas_frame = tk.Frame(master)
        self.canvas = None

        # Layout
        self.record_button.pack()
        self.playback_button.pack()
        self.canvas_frame.pack()

        # Data storage
        self.recorded_data = []

    def start_recording(self):
        # Simulate recording data (replace this with actual simulator integration)
        # For simplicity, we'll just generate some random data
        simulated_data = [{"x": i, "y": i**2} for i in range(10)]
        self.recorded_data.extend(simulated_data)

    def playback(self):
        if self.recorded_data:
            # Plot the recorded data
            fig, ax = plt.subplots()
            x = [point["x"] for point in self.recorded_data]
            y = [point["y"] for point in self.recorded_data]
            ax.plot(x, y)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')

            # Embed the plot in the Tkinter window
            if self.canvas:
                self.canvas.get_tk_widget().destroy()

            self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def main():
    root = tk.Tk()
    app = FlightRecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
