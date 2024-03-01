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
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Celestial body parameters
sun_radius = 50
earth_radius = 20
moon_radius = 10

# Orbital parameters
earth_orbit_radius = 200
moon_orbit_radius = 50

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earth-Sun-Moon Simulator")

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

# Create celestial bodies
sun = CelestialBody(YELLOW, sun_radius, 0, 0)
earth = CelestialBody(BLUE, earth_radius, earth_orbit_radius, 1)
moon = CelestialBody(WHITE, moon_radius, moon_orbit_radius, 5)

all_sprites = pygame.sprite.Group()
all_sprites.add(sun, earth, moon)

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
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
