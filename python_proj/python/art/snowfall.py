import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Snowfall Simulation")
clock = pygame.time.Clock()

class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(1, 4)
        self.color = WHITE
        self.velocity = self.radius / 2

    def fall(self):
        self.y += self.velocity

class Snowfall:
    def __init__(self):
        self.snowflakes = []

    def generate_snowflake(self):
        self.snowflakes.append(Snowflake())

    def update(self):
        for snowflake in self.snowflakes:
            snowflake.fall()

    def draw(self):
        for snowflake in self.snowflakes:
            pygame.draw.circle(screen, snowflake.color, (int(snowflake.x), int(snowflake.y)), snowflake.radius)

# Create a snowfall instance
snowfall = Snowfall()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate new snowflakes
    if random.random() < 0.1:
        snowfall.generate_snowflake()

    # Update
    snowfall.update()

    # Draw
    screen.fill(BLACK)
    snowfall.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
