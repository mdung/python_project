import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Define the 3D mathematical function
def mathematical_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Create initial data
x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x_values, y_values)
z = mathematical_function(x, y)

# Create the initial 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
initial_plot = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

# Create sliders for adjusting the cross-section
axcolor = 'lightgoldenrodyellow'
ax_x = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor=axcolor)
ax_y = plt.axes([0.25, 0.07, 0.65, 0.03], facecolor=axcolor)

slider_x = Slider(ax_x, 'X', x_values.min(), x_values.max(), valinit=0)
slider_y = Slider(ax_y, 'Y', y_values.min(), y_values.max(), valinit=0)

# Update function for sliders
def update(val):
    cross_section_x = slider_x.val
    cross_section_y = slider_y.val

    # Calculate the cross-sections
    cross_section_x_values = x_values
    cross_section_y_values = y_values
    cross_section_z_x = mathematical_function(cross_section_x_values, cross_section_y)
    cross_section_z_y = mathematical_function(cross_section_x, cross_section_y_values)

    # Update the 2D cross-section plots
    ax.cla()
    ax.plot(cross_section_x_values, cross_section_z_x, zs=cross_section_y, zdir='y', color='red', label='Cross-section X')
    ax.plot(cross_section_z_y, cross_section_y_values, zs=cross_section_x, zdir='x', color='blue', label='Cross-section Y')

    # Update the 3D surface plot
    initial_plot = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Function Cross-Sections')
    ax.legend()

# Attach the update function to the sliders
slider_x.on_changed(update)
slider_y.on_changed(update)

# Show the plot
plt.show()
