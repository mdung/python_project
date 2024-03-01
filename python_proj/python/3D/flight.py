import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_flight_path():
    # Generate a flight path for the plane
    t = np.linspace(0, 10, 100)
    x = np.sin(t)
    y = 2 * np.sin(2 * t)
    z = 0.5 * t

    return x, y, z

def plot_flight_plane(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the flight path
    ax.plot(x, y, z, label='Flight Path', linewidth=2)

    # Plot the plane
    ax.scatter(x[-1], y[-1], z[-1], color='red', marker='o', s=100, label='Plane')

    # Customize the plot
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Flight Plane Visualizer')
    ax.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    flight_path_x, flight_path_y, flight_path_z = generate_flight_path()
    plot_flight_plane(flight_path_x, flight_path_y, flight_path_z)
