import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the mathematical function to visualize
def mathematical_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = mathematical_function(x, y)

# Create a list of available colormaps
colormaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'twilight', 'twilight_shifted']

# Plot using different colormaps
fig, axes = plt.subplots(2, 4, figsize=(14, 7), subplot_kw={'projection': '3d'})
fig.suptitle('3D Mathematical Function Visualizer with Different Colormaps')

for ax, colormap in zip(axes.flat, colormaps):
    ax.plot_surface(x, y, z, cmap=colormap)
    ax.set_title(colormap)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()
