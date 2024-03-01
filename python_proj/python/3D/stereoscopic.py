import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_milky_way_model():
    # Generate 3D coordinates for a simplified Milky Way model
    # For simplicity, use basic spheres to represent stars in the Milky Way.
    # The sizes and distances are not to scale.

    # Milky Way center (galactic nucleus)
    galactic_nucleus_radius = 1e3  # arbitrary radius for representation
    galactic_nucleus_x, galactic_nucleus_y, galactic_nucleus_z = [0], [0], [0]

    # Generate random stars in the Milky Way
    num_stars = 500
    star_radius = 10  # arbitrary radius for representation
    star_distances = np.random.uniform(1e2, 1e4, num_stars)
    star_angles = np.random.uniform(0, 2 * np.pi, num_stars)

    star_x = star_distances * np.cos(star_angles)
    star_y = star_distances * np.sin(star_angles)
    star_z = np.random.uniform(-1e3, 1e3, num_stars)

    return (galactic_nucleus_x, galactic_nucleus_y, galactic_nucleus_z, galactic_nucleus_radius), \
           (star_x, star_y, star_z, star_radius)

def plot_3d_milky_way(galactic_nucleus, stars):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot galactic nucleus
    ax.scatter(*galactic_nucleus, color='red', label='Galactic Nucleus')

    # Plot stars in the Milky Way
    ax.scatter(*stars, color='white', alpha=0.5, label='Stars')

    # Customize the plot
    ax.set_xlabel('X-axis (light-years)')
    ax.set_ylabel('Y-axis (light-years)')
    ax.set_zlabel('Z-axis (light-years)')
    ax.set_title('3D Milky Way Visualizer')
    ax.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    galactic_nucleus, stars = generate_milky_way_model()
    plot_3d_milky_way(galactic_nucleus, stars)
