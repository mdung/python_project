import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Game")

# Player setup
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT - player_height - 20
player_speed = 5

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Update the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Refresh the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
