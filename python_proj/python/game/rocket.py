import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

# Rocket class
class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0
        self.thrust = 0

    def update(self):
        self.velocity += self.thrust
        self.rect.y -= self.velocity
        if self.rect.bottom < 0:
            self.kill()


# Particle class
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.size = size
        self.color = color
        self.fade_rate = random.uniform(0.1, 0.2)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 5)

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        self.size -= self.fade_rate
        if self.size <= 0:
            self.kill()


# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Exhaust Simulation")

# Groups for sprites
all_sprites = pygame.sprite.Group()
rockets = pygame.sprite.Group()
particles = pygame.sprite.Group()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn rockets
    if random.random() < 0.02:
        new_rocket = Rocket(random.randint(50, WIDTH - 50), HEIGHT)
        all_sprites.add(new_rocket)
        rockets.add(new_rocket)

    # Update sprites
    all_sprites.update()

    # Create particles for each rocket
    for rocket in rockets:
        exhaust_x = rocket.rect.centerx
        exhaust_y = rocket.rect.bottom
        for _ in range(10):
            particle = Particle(
                exhaust_x, exhaust_y, random.choice([ORANGE, YELLOW]), random.randint(2, 4)
            )
            all_sprites.add(particle)
            particles.add(particle)

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
