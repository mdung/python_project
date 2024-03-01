import pygame
from pygame.locals import *

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player Movement App")

clock = pygame.time.Clock()

# Player variables
player_x, player_y = width // 2, height // 2
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= player_speed
    if keys[K_RIGHT]:
        player_x += player_speed
    if keys[K_UP]:
        player_y -= player_speed
    if keys[K_DOWN]:
        player_y += player_speed

    # Keep the player within the screen boundaries
    player_x = max(0, min(player_x, width - 20))
    player_y = max(0, min(player_y, height - 20))

    # Draw to the screen
    screen.fill((255, 255, 255))  # Set background color
    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, 20, 20))  # Draw the player

    pygame.display.flip()
    clock.tick(60)  # Adjust frame rate

pygame.quit()
