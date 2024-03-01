import sys
import pygame
import random
from pygame.locals import QUIT

# Define constants
WIDTH, HEIGHT = 800, 600
NUM_BIRDS = 100
BOID_RADIUS = 5
SPEED = 5
ALIGNMENT_RADIUS = 50
COHESION_RADIUS = 100
SEPARATION_RADIUS = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Boid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

    def update(self, flock):
        alignment = self.align(flock)
        cohesion = self.cohere(flock)
        separation = self.separate(flock)

        # Update velocity
        self.dx += alignment[0] + cohesion[0] + separation[0]
        self.dy += alignment[1] + cohesion[1] + separation[1]

        # Limit speed
        speed = (self.dx**2 + self.dy**2)**0.5
        if speed > SPEED:
            factor = SPEED / speed
            self.dx *= factor
            self.dy *= factor

        # Update position
        self.x += self.dx
        self.y += self.dy

        # Wrap around edges
        self.x %= WIDTH
        self.y %= HEIGHT

    def align(self, flock):
        # Alignment: Adjust velocity based on the average velocity of nearby boids
        avg_dx = sum([boid.dx for boid in flock]) / len(flock)
        avg_dy = sum([boid.dy for boid in flock]) / len(flock)
        return avg_dx, avg_dy

    def cohere(self, flock):
        # Cohesion: Adjust velocity to move towards the center of mass of nearby boids
        center_x = sum([boid.x for boid in flock]) / len(flock)
        center_y = sum([boid.y for boid in flock]) / len(flock)
        return (center_x - self.x) / COHESION_RADIUS, (center_y - self.y) / COHESION_RADIUS

    def separate(self, flock):
        # Separation: Adjust velocity to avoid crowding with nearby boids
        separation_vector = [0, 0]
        for boid in flock:
            distance = ((self.x - boid.x)**2 + (self.y - boid.y)**2)**0.5
            if 0 < distance < SEPARATION_RADIUS:
                separation_vector[0] += (self.x - boid.x) / distance
                separation_vector[1] += (self.y - boid.y) / distance
        return separation_vector

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create a flock of boids
flock = [Boid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)) for _ in range(NUM_BIRDS)]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update boids
    for boid in flock:
        boid.update(flock)

    # Draw the flock
    screen.fill(BLACK)
    for boid in flock:
        pygame.draw.circle(screen, WHITE, (int(boid.x), int(boid.y)), BOID_RADIUS)

    pygame.display.flip()
    clock.tick(30)  # Adjust the frame rate as needed
