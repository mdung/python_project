import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TYPHOON_COLOR = (0, 0, 255)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typhoon Frequency and Intensity Simulation")
clock = pygame.time.Clock()

class Typhoon:
    def __init__(self, intensity):
        self.intensity = intensity
        self.radius = int(intensity * 5)
        self.center = (random.randint(self.radius, WIDTH - self.radius),
                       random.randint(self.radius, HEIGHT - self.radius))

    def draw(self):
        pygame.draw.circle(screen, TYPHOON_COLOR, self.center, self.radius)

# List to store typhoons
typhoons = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate the effects of climate change on typhoon frequency and intensity
    intensity = random.uniform(1.0, 9.0)
    new_typhoon = Typhoon(intensity)
    typhoons.append(new_typhoon)

    # Draw
    screen.fill(BLACK)

    # Draw all typhoons
    for typhoon in typhoons:
        typhoon.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
