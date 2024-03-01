# Import necessary libraries
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Function to evaluate k-means clustering quality using silhouette score
def evaluate_kmeans_silhouette(X, k_range):
    silhouette_scores = []

    for k in k_range:
        # Fit KMeans model
        kmeans = KMeans(n_clusters=k, random_state=0)
        labels = kmeans.fit_predict(X)

        # Compute silhouette score
        silhouette_avg = silhouette_score(X, labels)
        silhouette_scores.append(silhouette_avg)

        print(f"For n_clusters={k}, silhouette score: {silhouette_avg}")

    return silhouette_scores

# Define the range of cluster numbers to evaluate
k_range = range(2, 11)

# Evaluate k-means clustering using silhouette score
silhouette_scores = evaluate_kmeans_silhouette(X, k_range)

# Plot the silhouette scores
plt.plot(k_range, silhouette_scores, marker='o')
plt.title('Silhouette Score for K-Means Clustering')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.show()
