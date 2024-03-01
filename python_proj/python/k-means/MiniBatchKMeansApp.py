import tkinter as tk
from tkinter import filedialog
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MiniBatchKMeansApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-Batch K-Means Clustering")
        self.root.geometry("600x400")

        self.data = None
        self.labels = None
        self.centroids = None

        self.create_widgets()

    def create_widgets(self):
        # Load Data Button
        load_data_button = tk.Button(
            self.root, text="Load Data", command=self.load_data)
        load_data_button.pack(pady=10)

        # Cluster Button
        cluster_button = tk.Button(
            self.root, text="Cluster Data", command=self.cluster_data)
        cluster_button.pack(pady=10)

        # Display Plot
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def load_data(self):
        file_path = filedialog.askopenfilename(
            title="Select Data File", filetypes=[("CSV files", "*.csv")])

        if file_path:
            self.data = np.loadtxt(file_path, delimiter=',')
            tk.messagebox.showinfo("Data Loaded", "Data loaded successfully.")

    def cluster_data(self):
        if self.data is None:
            tk.messagebox.showwarning(
                "Data Not Loaded", "Please load data before clustering.")
            return

        num_clusters = tk.simpledialog.askinteger(
            "Number of Clusters", "Enter the number of clusters:", minvalue=1)

        if num_clusters is None:
            return

        # Perform Mini-Batch K-Means clustering
        kmeans = MiniBatchKMeans(n_clusters=num_clusters, random_state=42)
        self.labels = kmeans.fit_predict(self.data)
        self.centroids = kmeans.cluster_centers_

        # Plot the clustered data
        self.plot_clusters()

    def plot_clusters(self):
        self.ax.clear()

        for cluster in range(len(self.centroids)):
            cluster_points = self.data[self.labels == cluster]
            self.ax.scatter(
                cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {cluster + 1}')

        self.ax.scatter(
            self.centroids[:, 0], self.centroids[:, 1], marker='x', s=200, c='red', label='Centroids')
        self.ax.legend()
        self.ax.set_title("Mini-Batch K-Means Clustering")
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBatchKMeansApp(root)
    root.mainloop()
