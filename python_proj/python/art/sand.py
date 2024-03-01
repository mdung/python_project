import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SAND_COLOR = (194, 178, 128)
GRAVITY = 0.5

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Art Simulation")
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 2
        self.color = SAND_COLOR
        self.velocity = 0

    def fall(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# List to store particles
particles = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new particles on mouse click
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        particles.append(Particle(mx, my))

    # Update
    for particle in particles:
        particle.fall()

    # Draw
    screen.fill(BLACK)

    # Draw particles
    for particle in particles:
        particle.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
