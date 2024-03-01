import pygame
import sys
import random
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
EARTHQUAKE_COLOR = (255, 0, 0)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earthquake Simulation")
clock = pygame.time.Clock()

class Earthquake:
    def __init__(self, magnitude):
        self.magnitude = magnitude
        self.radius = int(magnitude * 10)
        self.center = (random.randint(self.radius, WIDTH - self.radius),
                       random.randint(self.radius, HEIGHT - self.radius))

    def draw(self):
        pygame.draw.circle(screen, EARTHQUAKE_COLOR, self.center, self.radius)

# List to store earthquakes
earthquakes = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate the occurrence of an earthquake with varying magnitudes
    magnitude = random.uniform(1.0, 9.0)
    new_earthquake = Earthquake(magnitude)
    earthquakes.append(new_earthquake)

    # Draw
    screen.fill(BLACK)

    # Draw all earthquakes
    for eq in earthquakes:
        eq.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
