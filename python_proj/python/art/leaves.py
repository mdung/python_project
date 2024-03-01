import pygame
import sys
import random
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leaf Motion Simulation")
clock = pygame.time.Clock()

# Leaf class
class Leaf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 128, 0), [(0, 10), (10, 0), (20, 10), (10, 20)])
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.angle = random.uniform(0, 360)
        self.angular_velocity = random.uniform(-1, 1)

    def update(self):
        self.rect.x += 1  # Adjust the horizontal speed as needed
        self.rect.y += math.sin(math.radians(self.angle)) * 2  # Simulate vertical motion
        self.angle += self.angular_velocity

        if not (0 < self.rect.x < WIDTH and 0 < self.rect.y < HEIGHT):
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = random.randint(0, HEIGHT)

# Sprite Group
all_sprites = pygame.sprite.Group()
leaves = [Leaf() for _ in range(50)]
all_sprites.add(leaves)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
