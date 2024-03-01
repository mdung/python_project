import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generate synthetic data
data, true_labels = make_blobs(n_samples=300, centers=4, random_state=42)

# Function to plot the clusters
def plot_clusters(data, labels, centroids, title):
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200)
    plt.title(title)
    plt.show()

# Function to perform k-means clustering with different initialization methods
def kmeans_with_initialization(data, n_clusters, init_method):
    kmeans = KMeans(n_clusters=n_clusters, init=init_method, random_state=42)
    labels = kmeans.fit_predict(data)
    centroids = kmeans.cluster_centers_
    score = silhouette_score(data, labels)
    plot_clusters(data, labels, centroids, f'{init_method} Initialization (Silhouette Score: {score:.2f})')

# Experiment with different initialization methods
initialization_methods = ['k-means++', 'random']
num_clusters = 4

for init_method in initialization_methods:
    kmeans_with_initialization(data, num_clusters, init_method)
