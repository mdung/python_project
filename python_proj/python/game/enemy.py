import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enemy Movement Patterns")

# Set up Pygame clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, movement_pattern):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.movement_pattern = movement_pattern
        self.angle = 0
        self.amplitude = random.randint(20, 50)
        self.speed = random.uniform(1, 3)

    def update(self):
        if self.movement_pattern == "linear":
            self.rect.x += self.speed
        elif self.movement_pattern == "sinusoidal":
            self.rect.x += self.speed
            self.rect.y = 200 + self.amplitude * math.sin(math.radians(self.angle))
            self.angle += 5
        elif self.movement_pattern == "random":
            self.rect.x += random.uniform(-self.speed, self.speed)
            self.rect.y += random.uniform(-self.speed, self.speed)

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create enemies with different movement patterns
linear_enemy = Enemy(100, 100, "linear")
sinusoidal_enemy = Enemy(100, 200, "sinusoidal")
random_enemy = Enemy(100, 300, "random")

# Add enemies to sprite group
all_sprites.add(linear_enemy, sinusoidal_enemy, random_enemy)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Clear screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
