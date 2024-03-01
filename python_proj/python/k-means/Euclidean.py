import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class HierarchicalClusteringApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hierarchical Clustering Experiment")

        # Variables
        self.data = None
        self.linkage_method_var = tk.StringVar()
        self.distance_metric_var = tk.StringVar()

        # UI components
        self.label_data = tk.Label(master, text="Enter data (comma-separated):")
        self.entry_data = tk.Entry(master)
        self.label_linkage = tk.Label(master, text="Linkage Method:")
        self.combobox_linkage = ttk.Combobox(master, values=["single", "complete", "average", "ward"])
        self.label_distance = tk.Label(master, text="Distance Metric:")
        self.combobox_distance = ttk.Combobox(master, values=["euclidean", "manhattan", "cosine"])
        self.button_cluster = tk.Button(master, text="Cluster", command=self.cluster_data)
        self.canvas = None

        # Layout
        self.label_data.grid(row=0, column=0, columnspan=2, pady=10)
        self.entry_data.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        self.label_linkage.grid(row=2, column=0, pady=10)
        self.combobox_linkage.grid(row=2, column=1, pady=10, padx=10, sticky="ew")
        self.label_distance.grid(row=3, column=0, pady=10)
        self.combobox_distance.grid(row=3, column=1, pady=10, padx=10, sticky="ew")
        self.button_cluster.grid(row=4, column=0, columnspan=2, pady=10)

    def cluster_data(self):
        # Get data from entry and convert to numpy array
        input_data = self.entry_data.get()
        try:
            self.data = np.array([list(map(float, row.split(','))) for row in input_data.split('\n')])
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input data. Please enter comma-separated numerical values.")
            return

        # Get selected linkage method and distance metric
        linkage_method = self.combobox_linkage.get()
        distance_metric = self.combobox_distance.get()

        # Perform hierarchical clustering
        Z = linkage(self.data, method=linkage_method, metric=distance_metric)

        # Display dendrogram
        self.display_dendrogram(Z)

    def display_dendrogram(self, Z):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # Create a new figure and canvas
        fig, ax = plt.subplots(figsize=(8, 6))
        dendrogram(Z)
        plt.title("Hierarchical Clustering Dendrogram")
        plt.xlabel("Data Points")
        plt.ylabel(f"{self.combobox_distance.get().capitalize()} Distance")
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    app = HierarchicalClusteringApp(root)
    root.mainloop()
