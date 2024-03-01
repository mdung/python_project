import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Earth parameters
earth_radius = 30

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seasons Simulator")

# Earth class
class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((earth_radius * 2, earth_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLUE, (earth_radius, earth_radius), earth_radius)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.angle = 0
        self.angular_speed = 0.1  # Angular speed for simplicity

    def update(self):
        self.angle += self.angular_speed
        self.rect.x = WIDTH // 2 + math.cos(math.radians(self.angle)) * 150
        self.rect.y = HEIGHT // 2 + math.sin(math.radians(self.angle)) * 150

# Main game loop
clock = pygame.time.Clock()

# Create Earth sprite
earth = Earth()
all_sprites = pygame.sprite.Group()
all_sprites.add(earth)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()

    # Draw
    screen.fill(YELLOW)  # Background color representing sunlight
    all_sprites.draw(screen)

    # Display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
