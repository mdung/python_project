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
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Classes
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = -self.rect.height
            self.speed = random.randint(1, 5)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Groups
all_sprites = pygame.sprite.Group()
towers = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            tower = Tower(x, y)
            all_sprites.add(tower)
            towers.add(tower)

    # Spawn enemies
    if random.randint(1, 100) < 5:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Update
    all_sprites.update()

    # Check for collisions (example: bullet hits enemy)
    hits = pygame.sprite.groupcollide(enemies, towers, False, False)
    for enemy, towers_hit in hits.items():
        for tower in towers_hit:
            print("Enemy hit by tower!")

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Refresh the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
