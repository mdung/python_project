import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function to visualize (example: 3D Gaussian)
def gaussian_3d(x, y):
    sigma = 1.0
    return np.exp(-(x**2 + y**2) / (2 * sigma**2))

# Generate data for the heatmap
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = gaussian_3d(X, Y)

# Create a 3D heatmap plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the heatmap
heatmap = ax.plot_surface(X, Y, Z, cmap='viridis', cstride=1, rstride=1, alpha=0.8, antialiased=True)

# Add colorbar
fig.colorbar(heatmap, ax=ax, shrink=0.6, aspect=10)

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Function Value')
ax.set_title('3D Heatmap of Function Values')

# Show the plot
plt.show()
