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

# Satellite parameters
satellite_radius = 20
satellite_speed = 2

# Ground Station parameters
ground_station_size = 20

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Satellite Communication Simulator")

# Satellite class
class Satellite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((satellite_radius * 2, satellite_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLUE, (satellite_radius, satellite_radius), satellite_radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def update(self):
        self.angle += satellite_speed
        self.rect.x = WIDTH // 2 + math.cos(math.radians(self.angle)) * (WIDTH // 3)
        self.rect.y = HEIGHT // 2 + math.sin(math.radians(self.angle)) * (HEIGHT // 3)

# Ground Station class
class GroundStation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ground_station_size * 2, ground_station_size * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (ground_station_size, ground_station_size), ground_station_size)
        self.rect = self.image.get_rect(center=(x, y))

# Create satellite and ground station
satellite = Satellite(WIDTH // 2, HEIGHT // 2)
ground_station = GroundStation(WIDTH // 2, HEIGHT // 2)

all_sprites = pygame.sprite.Group()
all_sprites.add(satellite, ground_station)

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
