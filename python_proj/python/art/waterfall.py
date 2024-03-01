import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Waterfall Visualization")
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 2
        self.color = BLUE
        self.velocity = 5

    def move(self):
        self.y += self.velocity

class Waterfall:
    def __init__(self, x, y):
        self.particles = [Particle(x, y) for _ in range(50)]

    def update(self):
        for particle in self.particles:
            particle.move()

    def draw(self):
        for particle in self.particles:
            pygame.draw.circle(screen, particle.color, (particle.x, particle.y), particle.radius)

# Create a waterfall instance
waterfall = Waterfall(WIDTH // 2, 0)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    waterfall.update()

    # Draw
    screen.fill(BLACK)
    waterfall.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
