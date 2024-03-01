import tkinter as tk
from tkinter import ttk
import timeit
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

class ClusteringEfficiencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clustering Efficiency Evaluation")

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label = ttk.Label(self.frame, text="Number of Data Points:")
        self.label.grid(column=0, row=0, sticky=tk.W, pady=5)

        self.data_points_entry = ttk.Entry(self.frame)
        self.data_points_entry.grid(column=1, row=0, pady=5)

        self.evaluate_button = ttk.Button(self.frame, text="Evaluate", command=self.evaluate_efficiency)
        self.evaluate_button.grid(column=0, row=1, columnspan=2, pady=10)

    def generate_random_data(self, num_points):
        return np.random.rand(num_points, 2)

    def evaluate_efficiency(self):
        num_points = int(self.data_points_entry.get())

        data = self.generate_random_data(num_points)

        linkage_methods = ['single', 'complete', 'average', 'weighted', 'centroid', 'median', 'ward']

        results = {}

        for method in linkage_methods:
            start_time = timeit.default_timer()
            linkage(data, method)
            elapsed_time = timeit.default_timer() - start_time
            results[method] = elapsed_time

        self.plot_results(results)

    def plot_results(self, results):
        plt.bar(results.keys(), results.values(), color='skyblue')
        plt.xlabel('Linkage Method')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Computational Efficiency of Hierarchical Clustering Linkage Methods')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClusteringEfficiencyApp(root)
    root.mainloop()
