# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Generate synthetic data for clustering
data, true_labels = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Visualize the original data
plt.scatter(data[:, 0], data[:, 1], s=50, cmap='viridis')
plt.title("Original Data")
plt.show()

# Apply K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=0)
cluster_labels = kmeans.fit_predict(data_scaled)

# Visualize the clustered data
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, marker='X', c='red')
plt.title("Clustered Data with K-Means")
plt.show()

# Evaluate the clustering performance using silhouette score
silhouette_avg = silhouette_score(data_scaled, cluster_labels)
print(f"Silhouette Score: {silhouette_avg:.2f}")
