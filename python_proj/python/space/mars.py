import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Celestial body parameters
earth_radius = 30
mars_radius = 25

# Orbital parameters
earth_orbit_radius = 200
mars_orbit_radius = 300

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mars Exploration Simulator")

# Celestial body classes
class CelestialBody(pygame.sprite.Sprite):
    def __init__(self, color, radius, orbit_radius, angular_speed):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.orbit_radius = orbit_radius
        self.angle = 0
        self.angular_speed = angular_speed

    def update(self):
        self.angle += self.angular_speed
        self.rect.x = WIDTH // 2 + math.cos(math.radians(self.angle)) * self.orbit_radius
        self.rect.y = HEIGHT // 2 + math.sin(math.radians(self.angle)) * self.orbit_radius

# Spacecraft class
class Spacecraft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, WHITE, [(0, 0), (5, 20), (10, 0)])
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.angle = 0
        self.angular_speed = 0.1  # Angular speed for simplicity

    def update(self):
        self.angle += self.angular_speed
        self.rect.x = WIDTH // 2 + math.cos(math.radians(self.angle)) * (earth_orbit_radius + 30)
        self.rect.y = HEIGHT // 2 + math.sin(math.radians(self.angle)) * (earth_orbit_radius + 30)

# Create celestial bodies and spacecraft
earth = CelestialBody(BLUE, earth_radius, earth_orbit_radius, 0.1)
mars = CelestialBody(RED, mars_radius, mars_orbit_radius, 0.05)
spacecraft = Spacecraft()

all_sprites = pygame.sprite.Group()
all_sprites.add(earth, mars, spacecraft)

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
