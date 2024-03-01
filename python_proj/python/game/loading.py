import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
SPINNER_COLOR = (0, 0, 0)
SPINNER_RADIUS = 30
SPINNER_SPEED = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Loading Screen")

# Loading spinner variables
spinner_angle = 0
clock = pygame.time.Clock()

# Loading screen loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background
    screen.fill(BG_COLOR)

    # Draw the loading spinner
    spinner_rect = pygame.Rect(WIDTH // 2 - SPINNER_RADIUS, HEIGHT // 2 - SPINNER_RADIUS, 2 * SPINNER_RADIUS, 2 * SPINNER_RADIUS)
    pygame.draw.arc(screen, SPINNER_COLOR, spinner_rect, spinner_angle, spinner_angle + 90, SPINNER_RADIUS)

    # Update spinner angle for animation
    spinner_angle += SPINNER_SPEED
    if spinner_angle >= 360:
        spinner_angle = 0

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
