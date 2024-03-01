import random

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision Detection Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5

# Set up enemy
enemy_size = 30
enemy_x = width // 2 - enemy_size // 2
enemy_y = 10
enemy_speed = 3

def draw_player(x, y):
    """Draw the player on the screen."""
    pygame.draw.rect(screen, RED, [x, y, player_size, player_size])

def draw_enemy(x, y):
    """Draw the enemy on the screen."""
    pygame.draw.rect(screen, BLACK, [x, y, enemy_size, enemy_size])

def check_collision(player_x, player_y, enemy_x, enemy_y, size):
    """Check for collision between player and enemy."""
    if player_x < enemy_x + size and player_x + player_size > enemy_x and \
            player_y < enemy_y + size and player_y + player_size > enemy_y:
        return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Update enemy position
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = 0
        enemy_x = random.randint(0, width - enemy_size)

    # Check for collision
    if check_collision(player_x, player_y, enemy_x, enemy_y, enemy_size):
        print("Game Over! Collision detected.")
        pygame.quit()
        sys.exit()

    # Clear screen
    screen.fill(WHITE)

    # Draw player and enemy
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
