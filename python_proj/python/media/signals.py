import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from rtlsdr import RtlSdr

class TVSignalMonitorApp:
    def __init__(self, master):
        self.master = master
        master.title("TV Signal Strength Monitor")

        self.create_widgets()

    def create_widgets(self):
        self.frequency_label = ttk.Label(self.master, text="Frequency (MHz):")
        self.frequency_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.frequency_entry = ttk.Entry(self.master)
        self.frequency_entry.grid(row=0, column=1, padx=5, pady=5)

        self.start_button = ttk.Button(self.master, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.grid(row=0, column=2, padx=5, pady=5)

        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def start_monitoring(self):
        try:
            frequency = float(self.frequency_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid frequency. Please enter a valid number.")
            return

        # Call function to monitor TV signal strength
        self.monitor_tv_signal(frequency)

    def monitor_tv_signal(self, frequency):
        # Configure RTL-SDR device
        sdr = RtlSdr()
        sdr.sample_rate = 2.048e6  # 2.048 MHz
        sdr.center_freq = frequency * 1e6
        sdr.gain = 'auto'

        # Read samples and plot signal strength
        num_samples = 1024
        samples = sdr.read_samples(num_samples)
        signal_strength = 20 * np.log10(np.abs(samples))

        # Plot signal strength
        self.ax.clear()
        self.ax.plot(np.arange(num_samples), signal_strength)
        self.ax.set_xlabel('Sample Index')
        self.ax.set_ylabel('Signal Strength (dB)')

        # Update canvas
        self.canvas.draw()

        # Close RTL-SDR device
        sdr.close()

def main():
    root = tk.Tk()
    app = TVSignalMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
