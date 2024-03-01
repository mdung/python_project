import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)  # Daytime color
NIGHT_BLUE = (0, 0, 128)  # Nighttime color

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day-to-Night Transition")

# Time variables
day_duration = 10  # in seconds
current_time = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(FPS) / 1000  # convert milliseconds to seconds

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update time
    current_time += dt

    # Calculate transition factor (0 to 1)
    transition_factor = min(1, current_time / day_duration)

    # Interpolate colors for the transition
    current_color = (
        int(BLUE[0] * (1 - transition_factor) + NIGHT_BLUE[0] * transition_factor),
        int(BLUE[1] * (1 - transition_factor) + NIGHT_BLUE[1] * transition_factor),
        int(BLUE[2] * (1 - transition_factor) + NIGHT_BLUE[2] * transition_factor),
    )

    # Update the screen
    screen.fill(current_color)

    # Refresh the screen
    pygame.display.flip()

    # Reset time and color for the next day-night cycle
    if current_time >= day_duration:
        current_time = 0

# Quit Pygame
pygame.quit()
sys.exit()
