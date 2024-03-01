import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
G = 0.1  # Gravitational constant

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Planet class
class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y, mass, radius, color):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.mass = mass
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

    def apply_force(self, force):
        self.acceleration += force / self.mass

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.rect.center = self.position
        self.acceleration *= 0  # Reset acceleration for the next iteration


# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")
clock = pygame.time.Clock()

# Create planets
sun = Planet(WIDTH // 2, HEIGHT // 2, 100000, 50, YELLOW)
earth = Planet(WIDTH // 2 + 200, HEIGHT // 2, 100, 20, BLUE)

# Sprite groups
all_sprites = pygame.sprite.Group(sun, earth)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gravitational force calculation
    distance_vector = sun.position - earth.position
    distance = max(1, distance_vector.length())
    gravitational_force = G * (sun.mass * earth.mass) / (distance ** 2)
    gravitational_force_direction = distance_vector.normalize()
    gravitational_force_vector = gravitational_force * gravitational_force_direction

    # Apply gravitational force to the Earth
    earth.apply_force(gravitational_force_vector)

    # Update sprites
    all_sprites.update()

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Refresh screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
