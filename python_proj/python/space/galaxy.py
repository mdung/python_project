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

# Particle class representing stars
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(1, 3)
        self.color = WHITE

    def move(self):
        self.x += random.uniform(-0.5, 0.5)
        self.y += random.uniform(-0.5, 0.5)

# Function to calculate distance between two particles
def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Function to simulate gravity between particles
def apply_gravity(particles):
    for p1 in particles:
        for p2 in particles:
            if p1 != p2:
                distance = calculate_distance(p1, p2)
                if distance < 50:
                    # Apply gravitational force
                    force = 0.1 / distance**2
                    angle = math.atan2(p2.y - p1.y, p2.x - p1.x)
                    p1.x += force * math.cos(angle)
                    p1.y += force * math.sin(angle)

# Create particles (stars) randomly distributed in the window
particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(300)]

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Simulation")
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    apply_gravity(particles)

    # Clear the screen
    screen.fill(BLACK)

    # Draw particles
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.size)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
