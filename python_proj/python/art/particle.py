import sys
import pygame
import random
from pygame.locals import QUIT

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 60

class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = -10
        self.exploded = False
        self.particles = []

    def launch(self):
        self.exploded = True
        for _ in range(100):
            angle = random.uniform(0, 2 * 3.1416)
            speed = random.uniform(2, 10)
            particle = {'x': self.x, 'y': self.y, 'dx': speed * pygame.math.Vector2(math.cos(angle), math.sin(angle)).x, 'dy': speed * pygame.math.Vector2(math.cos(angle), math.sin(angle)).y, 'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}
            self.particles.append(particle)

    def update(self):
        if not self.exploded:
            self.y += self.dy
            if self.y <= HEIGHT / 2:
                self.launch()
        else:
            for particle in self.particles:
                particle['x'] += particle['dx']
                particle['y'] += particle['dy']

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create a list to store fireworks
fireworks = []

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update fireworks
    for firework in fireworks:
        firework.update()

    # Remove fireworks that have finished exploding
    fireworks = [firework for firework in fireworks if not (firework.exploded and not firework.particles)]

    # Generate new fireworks randomly
    if random.randint(0, 100) < 5:
        fireworks.append(Firework(random.randint(0, WIDTH), HEIGHT))

    # Draw the fireworks
    screen.fill((0, 0, 0))
    for firework in fireworks:
        if not firework.exploded:
            pygame.draw.circle(screen, (255, 255, 255), (int(firework.x), int(firework.y)), 5)
        else:
            for particle in firework.particles:
                pygame.draw.circle(screen, particle['color'], (int(particle['x']), int(particle['y'])), 2)

    pygame.display.flip()
    clock.tick(FPS)
