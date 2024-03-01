import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Particle class for simulating particles in the nebula
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = random.randint(1, 5)
        self.color = RED

    def update(self):
        self.radius += 1
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        if self.radius > 50:
            self.kill()

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetary Nebula Simulation")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new particles at random positions
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    particle = Particle(x, y)
    all_sprites.add(particle)

    # Update sprites
    all_sprites.update()

    # Refresh screen
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Limit frames per second
    clock.tick(FPS)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
