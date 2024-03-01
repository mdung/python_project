import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Planet class
class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius

# Ring class
class Ring(pygame.sprite.Sprite):
    def __init__(self, planet, distance, width, color):
        super().__init__()
        self.image = pygame.Surface((planet.radius * 2 + distance * 2, planet.radius * 2 + distance * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (planet.radius + distance, planet.radius + distance), planet.radius + width)
        self.rect = self.image.get_rect(center=planet.rect.center)

# Create Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetary Rings Simulation")
clock = pygame.time.Clock()

# Create planet
planet = Planet(WIDTH // 2, HEIGHT // 2, 30)

# Create rings
num_rings = 5
rings = pygame.sprite.Group()
for _ in range(num_rings):
    distance = random.randint(50, 150)
    width = random.randint(10, 30)
    color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
    ring = Ring(planet, distance, width, color)
    rings.add(ring)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw
    screen.fill(BLACK)
    screen.blit(planet.image, planet.rect)

    rings.update()
    rings.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
