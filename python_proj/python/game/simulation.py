import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Simulation")

# Water variables
water_height = [HEIGHT // 2] * WIDTH
damping = 0.99

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(FPS) / 1000  # convert milliseconds to seconds

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update water simulation
    new_water_height = water_height.copy()

    for i in range(1, WIDTH - 1):
        new_water_height[i] = (
                                      water_height[i]
                                      + (water_height[i - 1] + water_height[i + 1] - 2 * water_height[i]) * 0.5
                              ) * damping

    water_height = new_water_height

    # Draw water surface
    screen.fill(WHITE)
    for i in range(WIDTH):
        pygame.draw.line(screen, BLUE, (i, HEIGHT), (i, water_height[i]))

    # Refresh the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
