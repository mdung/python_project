import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CustomerSegmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Segmentation App")

        # Create Frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Add Buttons
        self.load_data_button = tk.Button(self.frame, text="Load Customer Data", command=self.load_data)
        self.load_data_button.pack(pady=10)

        self.cluster_button = tk.Button(self.frame, text="Cluster Customers", command=self.cluster_customers)
        self.cluster_button.pack(pady=10)

        # Initialize DataFrame
        self.customer_data = pd.DataFrame()
        self.clustered_data = None

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select Customer Dataset CSV file",
                                               filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.customer_data = pd.read_csv(file_path)
            tk.messagebox.showinfo("Success", "Customer dataset loaded successfully!")

    def cluster_customers(self):
        if self.customer_data.empty:
            tk.messagebox.showwarning("Warning", "Please load customer data first.")
            return

        # Preprocess data and perform k-means clustering
        X = self.customer_data.drop(['CustomerID'], axis=1)

        # Let's assume you want to identify 3 customer segments
        n_clusters = 3
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.clustered_data = self.customer_data.copy()
        self.clustered_data['Cluster'] = kmeans.fit_predict(X)

        tk.messagebox.showinfo("Clustering Results", "Customer clustering completed!")

        # Visualize the clustered data
        self.visualize_clusters()

    def visualize_clusters(self):
        # Plot a scatter plot of two features (you can customize based on your data)
        plt.figure(figsize=(8, 6))
        plt.scatter(self.clustered_data['Feature1'], self.clustered_data['Feature2'], c=self.clustered_data['Cluster'], cmap='viridis')
        plt.title('Customer Segmentation')
        plt.xlabel('Feature1')
        plt.ylabel('Feature2')

        # Display the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerSegmentationApp(root)
    root.mainloop()
