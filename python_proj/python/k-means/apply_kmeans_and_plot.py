import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Function to apply k-means clustering and plot results
def apply_kmeans_and_plot(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)

    # Get cluster centers and labels
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Plot the clustered dataset
    plt.scatter(X[:, 0], X[:, 1], c=labels, marker='o', edgecolors='black', cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Cluster Centers')
    plt.title(f'K-Means Clustering with {n_clusters} Clusters')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

# Generate synthetic dataset
n_samples = 300
n_features = 2
n_clusters_list = [2, 3, 4, 5]  # Try different numbers of clusters

# Create synthetic dataset with make_blobs
X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=max(n_clusters_list), random_state=42)

# Plot the original synthetic dataset
plt.scatter(X[:, 0], X[:, 1], c='blue', marker='o', edgecolors='black')
plt.title('Synthetic Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Apply k-means clustering with different numbers of clusters
for n_clusters in n_clusters_list:
    apply_kmeans_and_plot(X, n_clusters)
