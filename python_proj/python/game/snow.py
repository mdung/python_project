import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Snowflake class
class Snowflake(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.size = size

    def update(self):
        self.rect.y += 1  # Move snowflake downward
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-self.size, 0)
            self.rect.x = random.randint(0, WIDTH)


# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Snow Accumulation Simulation")

# Groups for sprites
all_sprites = pygame.sprite.Group()
snowflakes = pygame.sprite.Group()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn snowflakes
    if len(snowflakes) < 300:
        for _ in range(10):
            snowflake = Snowflake(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(2, 5))
            all_sprites.add(snowflake)
            snowflakes.add(snowflake)

    # Update sprites
    all_sprites.update()

    # Draw background
    screen.fill((0, 0, 50))  # Dark blue background

    # Draw sprites
    all_sprites.draw(screen)

    # Check for snow accumulation on the ground
    for y in range(HEIGHT - 1, 0, -1):
        for x in range(WIDTH):
            pixel_color = screen.get_at((x, y))
            if pixel_color == (0, 0, 50):  # Dark blue background
                accumulated_snow = sum(1 for flake in snowflakes if flake.rect.collidepoint(x, y))
                if accumulated_snow > 5:
                    pygame.draw.circle(screen, WHITE, (x, y), accumulated_snow // 5)

    # Refresh the screen
    pygame.display.flip()

    # Remove old snowflakes
    snowflakes = pygame.sprite.Group([flake for flake in snowflakes if flake.rect.y < HEIGHT])

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
