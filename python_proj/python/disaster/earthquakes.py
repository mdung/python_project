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
BUILDING_COLOR = (100, 100, 100)
BUILDING_WIDTH = 30
BUILDING_HEIGHT_RANGE = (50, 300)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earthquake Impact Simulation")
clock = pygame.time.Clock()

class Building:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(*BUILDING_HEIGHT_RANGE)
        self.y = HEIGHT - self.height
        self.rect = pygame.Rect(self.x, self.y, BUILDING_WIDTH, self.height)

    def draw(self):
        pygame.draw.rect(screen, BUILDING_COLOR, self.rect)

class Earthquake:
    def __init__(self, magnitude):
        self.magnitude = magnitude
        self.radius = int(magnitude * 10)
        self.center = (random.randint(self.radius, WIDTH - self.radius),
                       random.randint(self.radius, HEIGHT - self.radius))

    def draw(self):
        pygame.draw.circle(screen, EARTHQUAKE_COLOR, self.center, self.radius)

# List to store buildings and earthquakes
buildings = [Building(i * (BUILDING_WIDTH + 10)) for i in range(WIDTH // (BUILDING_WIDTH + 10))]
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

    # Draw all buildings
    for building in buildings:
        building.draw()

    # Draw all earthquakes
    for eq in earthquakes:
        eq.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
