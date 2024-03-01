import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player properties
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load player and obstacle images
player_image = pygame.Surface((player_width, player_height))
player_image.fill(BLUE)

obstacle_image = pygame.Surface((obstacle_width, obstacle_height))
obstacle_image.fill(WHITE)

# Lists to store obstacles
obstacles = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Obstacle spawning
    if pygame.time.get_ticks() % obstacle_frequency == 0:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - obstacle_height - 20
        obstacles.append((obstacle_x, obstacle_y))

    # Obstacle movement
    for i, obstacle in enumerate(obstacles):
        obstacles[i] = (obstacle[0] - obstacle_speed, obstacle[1])

        # Collision check
        if (
                player_x < obstacle[0] + obstacle_width
                and player_x + player_width > obstacle[0]
                and player_y < obstacle[1] + obstacle_height
                and player_y + player_height > obstacle[1]
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Remove off-screen obstacles
        if obstacle[0] < 0:
            obstacles.pop(i)

    # Update the display
    screen.fill((0, 0, 0))  # Fill with black background
    screen.blit(player_image, (player_x, player_y))  # Draw player

    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)  # Draw obstacles

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)
