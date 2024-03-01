# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                       columns= iris['feature_names'] + ['target'])

# Extract features and target
X = iris_df.iloc[:, :-1].values

# Apply hierarchical clustering
linkage_matrix = linkage(X, method='ward')
dendrogram(linkage_matrix)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

# Fit Agglomerative Clustering model
num_clusters = 3  # Number of clusters, based on the dendrogram
hierarchical_clustering = AgglomerativeClustering(n_clusters=num_clusters, affinity='euclidean', linkage='ward')
iris_df['cluster'] = hierarchical_clustering.fit_predict(X)

# Visualize the clusters
sns.pairplot(iris_df, hue='cluster', palette='Dark2', diag_kind='kde')
plt.show()
