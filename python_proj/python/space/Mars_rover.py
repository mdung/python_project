import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rover class
class Rover:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 5
        self.color = WHITE
        self.radius = 20

    def move(self):
        radian_angle = math.radians(self.angle)
        self.x += self.speed * math.cos(radian_angle)
        self.y += self.speed * math.sin(radian_angle)

    def avoid_obstacle(self, obstacles):
        for obstacle in obstacles:
            distance = math.sqrt((obstacle.x - self.x)**2 + (obstacle.y - self.y)**2)
            if distance < self.radius + obstacle.radius:
                # Obstacle detected, change direction
                self.angle += math.radians(45)  # Turn 45 degrees

# Obstacle class
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 30
        self.color = RED

# Create rover and obstacles
rover = Rover(WIDTH // 2, HEIGHT // 2)
obstacles = [Obstacle(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)) for _ in range(5)]

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mars Rover Simulation")
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rover.angle -= math.radians(5)
    if keys[pygame.K_RIGHT]:
        rover.angle += math.radians(5)

    rover.avoid_obstacle(obstacles)
    rover.move()

    # Clear the screen
    screen.fill(BLACK)

    # Draw rover
    pygame.draw.circle(screen, rover.color, (int(rover.x), int(rover.y)), rover.radius)
    pygame.draw.line(screen, rover.color, (rover.x, rover.y), (rover.x + rover.radius*math.cos(rover.angle),
                                                               rover.y + rover.radius*math.sin(rover.angle)))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.circle(screen, obstacle.color, (int(obstacle.x), int(obstacle.y)), obstacle.radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
