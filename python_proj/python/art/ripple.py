import pygame
import sys
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RADIUS = 10
WAVE_SPEED = 5

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ripple Tank Simulation")
clock = pygame.time.Clock()

class Source:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate_wave(self, waves):
        waves.append(Wave(self.x, self.y))

class Wave:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0

    def propagate(self):
        self.radius += WAVE_SPEED

    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), self.radius, 1)

# List to store waves
waves = []

# List to store sources
sources = [Source(100, 100), Source(300, 300), Source(500, 100)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate new waves
    for source in sources:
        if pygame.mouse.get_pressed()[0]:
            source.x, source.y = pygame.mouse.get_pos()
            source.generate_wave(waves)

    # Update
    for wave in waves:
        wave.propagate()

    # Draw
    screen.fill(BLACK)

    # Draw waves
    for wave in waves:
        wave.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
