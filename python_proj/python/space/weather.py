import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from spacepy import omni
from spacepy import time as spt
import numpy as np

class SpaceWeatherMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Weather Monitor")

        self.time_span_label = ttk.Label(root, text="Time Span (hours):")
        self.time_span_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.time_span_entry = ttk.Entry(root)
        self.time_span_entry.grid(row=0, column=1, padx=10, pady=10)

        self.fetch_button = ttk.Button(root, text="Fetch Data", command=self.fetch_space_weather_data)
        self.fetch_button.grid(row=0, column=2, padx=10, pady=10)

        self.plot_button = ttk.Button(root, text="Plot Data", command=self.plot_space_weather_data)
        self.plot_button.grid(row=0, column=3, padx=10, pady=10)

        self.quit_button = ttk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.grid(row=0, column=4, padx=10, pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=5, padx=10, pady=10)

    def fetch_space_weather_data(self):
        try:
            time_span_hours = int(self.time_span_entry.get())
            end_time = datetime.utcnow()
            start_time = end_time - timedelta(hours=time_span_hours)

            data = omni.get_omni(start_time, end_time, cdf=True)
            self.space_weather_data = data

            tk.messagebox.showinfo("Success", "Space weather data fetched successfully.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error fetching space weather data:\n{str(e)}")

    def plot_space_weather_data(self):
        if not hasattr(self, 'space_weather_data'):
            tk.messagebox.showwarning("Warning", "Please fetch space weather data first.")
            return

        self.ax.clear()

        time = self.space_weather_data['Epoch']
        kp_index = self.space_weather_data['KP']
        ap_index = self.space_weather_data['ap']

        self.ax.plot(time, kp_index, label='KP Index', color='blue')
        self.ax.plot(time, ap_index, label='Ap Index', color='green')

        self.ax.set_xlabel('Time (UTC)')
        self.ax.set_ylabel('Index Value')
        self.ax.set_title('Space Weather Monitoring')

        self.ax.legend()
        self.ax.grid(True)

        self.canvas.draw()

    def quit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceWeatherMonitorApp(root)
    root.mainloop()
