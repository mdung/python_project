import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Effect with Parallax Scrolling")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up background layers
bg_layer1 = pygame.image.load("background_layer1.png").convert()
bg_layer2 = pygame.image.load("background_layer2.png").convert()
bg_layer3 = pygame.image.load("background_layer3.png").convert()

# Set up player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5

# Set up clock
clock = pygame.time.Clock()

def draw_player(x, y):
    """Draw the player on the screen."""
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Update background layers for parallax scrolling
    screen.blit(bg_layer1, (0, 0))
    screen.blit(bg_layer2, (0, 0))
    screen.blit(bg_layer3, (0, 0))

    # Draw player
    draw_player(player_x, player_y)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
