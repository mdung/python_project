import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PARTICLE_COUNT = 1000

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = np.random.randint(0, 255, 3)
        self.size = 2

    def move(self, velocity):
        self.x += velocity[0]
        self.y += velocity[1]

        # Wrap around screen
        self.x %= WIDTH
        self.y %= HEIGHT

# Create particles
particles = [Particle(np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)) for _ in range(PARTICLE_COUNT)]

# Set up Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fluid Simulation")

# Main loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    for particle in particles:
        velocity = np.random.uniform(-1, 1, 2)
        particle.move(velocity)

    # Draw particles
    screen.fill(BLACK)
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.size)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
