import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dynamic Camera System Game")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height // 2 - player_size // 2
player_speed = 5

# Set up camera
camera_x = 0
camera_y = 0

# Set up clock
clock = pygame.time.Clock()

def draw_player(x, y):
    """Draw the player on the screen."""
    pygame.draw.rect(screen, RED, [x - camera_x, y - camera_y, player_size, player_size])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    player_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    # Update camera based on player's position
    camera_x = player_x - width // 2
    camera_y = player_y - height // 2

    # Clear screen
    screen.fill(WHITE)

    # Draw player with adjusted position based on camera
    draw_player(player_x, player_y)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
