import tkinter as tk
from tkinter import filedialog
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HierarchicalClusteringVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Dendrogram Visualizer")

        self.label = tk.Label(self.master, text="Select a CSV file with data:")
        self.label.pack()

        self.file_button = tk.Button(self.master, text="Browse", command=self.browse_file)
        self.file_button.pack()

        self.visualize_button = tk.Button(self.master, text="Visualize Dendrogram", command=self.visualize_dendrogram)
        self.visualize_button.pack()

        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_label = tk.Label(self.master, text=f"Selected file: {file_path}")
            self.file_label.pack()
            self.data = self.load_data(file_path)

    def visualize_dendrogram(self):
        if hasattr(self, 'data') and self.data is not None:
            # Perform hierarchical clustering
            linkage_matrix = linkage(self.data, method='ward')

            # Plot dendrogram
            dendrogram(linkage_matrix, labels=list(range(1, len(self.data) + 1)))
            plt.xlabel("Data Points")
            plt.ylabel("Distance")
            plt.title("Dendrogram Visualization")
            self.canvas.draw()
        else:
            self.show_error("Please select a valid CSV file.")

    def load_data(self, file_path):
        try:
            import pandas as pd
            data = pd.read_csv(file_path)
            return data.values
        except Exception as e:
            self.show_error(f"Error loading data: {str(e)}")

    def show_error(self, message):
        error_label = tk.Label(self.master, text=f"Error: {message}", fg="red")
        error_label.pack()

def main():
    root = tk.Tk()
    app = HierarchicalClusteringVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
