import tkinter as tk
from tkinter import ttk
import sqlite3
import numpy as np

class MonteCarloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monte Carlo Simulation for Risk Analysis")

        # Database setup
        self.conn = sqlite3.connect('monte_carlo_data.db')
        self.create_table()

        # GUI components
        self.create_widgets()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS simulations
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           mean REAL,
                           std_dev REAL,
                           num_simulations INTEGER,
                           results TEXT)''')
        self.conn.commit()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Mean:").grid(row=0, column=0, sticky="e")
        self.mean_entry = ttk.Entry(input_frame)
        self.mean_entry.grid(row=0, column=1, sticky="w")

        ttk.Label(input_frame, text="Standard Deviation:").grid(row=1, column=0, sticky="e")
        self.std_dev_entry = ttk.Entry(input_frame)
        self.std_dev_entry.grid(row=1, column=1, sticky="w")

        ttk.Label(input_frame, text="Number of Simulations:").grid(row=2, column=0, sticky="e")
        self.num_simulations_entry = ttk.Entry(input_frame)
        self.num_simulations_entry.grid(row=2, column=1, sticky="w")

        simulate_button = ttk.Button(input_frame, text="Simulate", command=self.run_simulation)
        simulate_button.grid(row=3, columnspan=2)

        # Output Frame
        output_frame = ttk.Frame(self.root, padding="10")
        output_frame.grid(row=1, column=0, padx=10, pady=10)

        self.results_text = tk.Text(output_frame, height=10, width=50, wrap="word")
        self.results_text.grid(row=0, column=0)

    def run_simulation(self):
        try:
            mean = float(self.mean_entry.get())
            std_dev = float(self.std_dev_entry.get())
            num_simulations = int(self.num_simulations_entry.get())

            # Perform Monte Carlo simulation
            results = self.monte_carlo_simulation(mean, std_dev, num_simulations)

            # Save results to the database
            self.save_results_to_db(mean, std_dev, num_simulations, results)

            # Display results in the text widget
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, results)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def monte_carlo_simulation(self, mean, std_dev, num_simulations):
        # Using NumPy for the Monte Carlo simulation
        simulations = np.random.normal(mean, std_dev, num_simulations)
        return f"Mean: {np.mean(simulations):.4f}\nStandard Deviation: {np.std(simulations):.4f}"

    def save_results_to_db(self, mean, std_dev, num_simulations, results):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO simulations (mean, std_dev, num_simulations, results) VALUES (?, ?, ?, ?)",
                       (mean, std_dev, num_simulations, results))
        self.conn.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MonteCarloApp(root)
    root.mainloop()
