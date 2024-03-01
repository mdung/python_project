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
RED = (255, 0, 0)
GRAY = (169, 169, 169)

# Celestial body parameters
sun_radius = 50
planet_radius = [5, 10, 12, 15, 18, 20]  # Mercury to Mars
moon_radius = 3

# Orbital parameters
planet_orbit_radius = [80, 120, 160, 200, 240, 280]  # Mercury to Mars
moon_orbit_radius = 20

# Angular speeds (for simplicity, not to scale)
angular_speeds = [1, 0.5, 0.4, 0.3, 0.2, 0.1]  # Sun, Mercury to Mars

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulator")

# Celestial body classes
class CelestialBody(pygame.sprite.Sprite):
    def __init__(self, color, radius, orbit_radius, angular_speed, name):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.orbit_radius = orbit_radius
        self.angle = 0
        self.angular_speed = angular_speed
        self.name = name

    def update(self):
        self.angle += self.angular_speed
        self.rect.x = WIDTH // 2 + math.cos(math.radians(self.angle)) * self.orbit_radius
        self.rect.y = HEIGHT // 2 + math.sin(math.radians(self.angle)) * self.orbit_radius

    def draw_name(self, screen):
        font = pygame.font.Font(None, 24)
        text = font.render(self.name, True, WHITE)
        text_rect = text.get_rect(center=(self.rect.x + self.rect.width + 10, self.rect.centery))
        screen.blit(text, text_rect)

# Create celestial bodies
sun = CelestialBody(YELLOW, sun_radius, 0, 0, "Sun")
mercury = CelestialBody(GRAY, planet_radius[0], planet_orbit_radius[0], angular_speeds[0], "Mercury")
venus = CelestialBody(RED, planet_radius[1], planet_orbit_radius[1], angular_speeds[1], "Venus")
earth = CelestialBody(BLUE, planet_radius[2], planet_orbit_radius[2], angular_speeds[2], "Earth")
mars = CelestialBody(RED, planet_radius[3], planet_orbit_radius[3], angular_speeds[3], "Mars")
moon = CelestialBody(WHITE, moon_radius, moon_orbit_radius, angular_speeds[4], "Moon")

all_sprites = pygame.sprite.Group()
all_sprites.add(sun, mercury, venus, earth, mars, moon)

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

    # Draw planet names
    for planet in [mercury, venus, earth, mars, moon]:
        planet.draw_name(screen)

    # Display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
