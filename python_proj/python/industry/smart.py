import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

class EnergySimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Consumption Simulation in Smart Buildings")

        # Database setup
        self.conn = sqlite3.connect('energy_data.db')
        self.create_table()

        # GUI components
        self.create_widgets()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS energy_data
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           timestamp TEXT,
                           consumption REAL)''')
        self.conn.commit()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Energy Consumption:").grid(row=0, column=0, sticky="e")
        self.consumption_entry = ttk.Entry(input_frame)
        self.consumption_entry.grid(row=0, column=1, sticky="w")

        record_button = ttk.Button(input_frame, text="Record Data", command=self.record_energy_data)
        record_button.grid(row=1, columnspan=2)

        # Plot Frame
        plot_frame = ttk.Frame(self.root, padding="10")
        plot_frame.grid(row=1, column=0, padx=10, pady=10)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=plot_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Display initial plot
        self.plot_energy_data()

    def record_energy_data(self):
        try:
            consumption = float(self.consumption_entry.get())

            # Save data to the database
            self.save_energy_data_to_db(consumption)

            # Update and redraw the plot
            self.plot_energy_data()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def save_energy_data_to_db(self, consumption):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO energy_data (timestamp, consumption) VALUES (?, ?)", (timestamp, consumption))
        self.conn.commit()

    def plot_energy_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT timestamp, consumption FROM energy_data")
        data = cursor.fetchall()

        timestamps, consumption_values = zip(*data)

        # Clear previous plot
        self.ax.clear()

        # Plot new data
        self.ax.plot(timestamps, consumption_values, marker='o')
        self.ax.set_xlabel('Timestamp')
        self.ax.set_ylabel('Energy Consumption')
        self.ax.set_title('Energy Consumption Simulation')

        # Redraw canvas
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = EnergySimulationApp(root)
    root.mainloop()
