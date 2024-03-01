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
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

# Particle class
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, speed):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.size = size
        self.speed = speed

    def update(self):
        self.size -= self.speed
        if self.size <= 0:
            self.kill()
        else:
            self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2), self.size // 2)
            self.rect = self.image.get_rect(center=self.rect.center)


# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explosion Shockwave Simulation")

# Groups for sprites
all_sprites = pygame.sprite.Group()
particles = pygame.sprite.Group()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn explosion at mouse position
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for _ in range(50):
            particle = Particle(
                mouse_x,
                mouse_y,
                random.choice([RED, ORANGE, YELLOW]),
                random.randint(5, 15),
                random.uniform(0.2, 0.5),
            )
            all_sprites.add(particle)
            particles.add(particle)

    # Update sprites
    all_sprites.update()

    # Draw background
    screen.fill(BLACK)

    # Draw sprites
    all_sprites.draw(screen)

    # Remove old particles
    particles = pygame.sprite.Group([particle for particle in particles if particle.size > 0])

    # Refresh the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
