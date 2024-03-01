import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ClimateDataAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Climate Data Analyzer")

        # Create menu
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open CSV", command=self.load_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        # Create widgets
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas_frame = tk.Frame(self.frame)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.info_label = tk.Label(self.frame, text="Select 'File' -> 'Open CSV' to load data.")
        self.info_label.pack(pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

        if file_path:
            try:
                df = pd.read_csv(file_path)
                self.plot_data(df)
            except Exception as e:
                self.info_label.config(text=f"Error loading CSV: {e}")

    def plot_data(self, df):
        self.info_label.config(text="Data loaded successfully. Plotting...")

        # Example: Plotting a time series
        plt.figure(figsize=(10, 5))
        sns.lineplot(x='Date', y='Temperature', data=df)
        plt.title('Temperature Time Series')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.xticks(rotation=45)

        # Embed the plot in the Tkinter window
        self.plot_canvas = FigureCanvasTkAgg(plt.gcf(), master=self.canvas_frame)
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Update the info label
        self.info_label.config(text="Data loaded and plotted successfully.")

        # Add other visualization and analysis components as needed


if __name__ == "__main__":
    root = tk.Tk()
    app = ClimateDataAnalyzer(root)
    root.geometry("800x600")
    root.mainloop()
