import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define mathematical functions to transition between
def function1(x):
    return np.sin(x)

def function2(x):
    return np.cos(x)

def function3(x):
    return np.exp(-x) * np.cos(2 * np.pi * x)

# Interpolation function for smooth transitions
def interpolate_functions(t, func1, func2):
    return (1 - t) * func1 + t * func2

# Animation update function
def update(frame):
    t = frame / total_frames
    y = interpolate_functions(t, function1(x_values), function2(x_values))
    line.set_ydata(y)
    return line,

if __name__ == "__main__":
    # Generate x values
    x_values = np.linspace(0, 4 * np.pi, 1000)

    # Set up the initial plot
    fig, ax = plt.subplots()
    line, = ax.plot(x_values, function1(x_values), label='Function 1', color='blue')

    # Customize the plot
    ax.set_title('Animated Transition Between Mathematical Functions')
    ax.legend()

    # Set up animation parameters
    total_frames = 100
    animation = FuncAnimation(fig, update, frames=total_frames, interval=50, blit=True)

    # Show the animated plot
    plt.show()
