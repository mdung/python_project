import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def parametric_surface(u, v):
    x = u
    y = v
    z = np.sin(u) + np.cos(v)
    return x, y, z

def visualize_parametric_surface():
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)

    x, y, z = parametric_surface(u, v)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Parametric Surface Visualization')

    plt.show()

if __name__ == "__main__":
    visualize_parametric_surface()
