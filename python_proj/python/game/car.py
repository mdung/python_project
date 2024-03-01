import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CAR_WIDTH, CAR_HEIGHT = 50, 100

# Player car class
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.image, RED, (0, 0, CAR_WIDTH, CAR_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Enemy car class
class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.image, GREEN, (0, 0, CAR_WIDTH, CAR_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - CAR_WIDTH)
        self.rect.y = random.randrange(-CAR_HEIGHT, -10)
        self.speed = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-CAR_HEIGHT, -10)
            self.rect.x = random.randrange(WIDTH - CAR_WIDTH)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Car Game")

# Create player car
player_car = PlayerCar()

# Create enemy cars
enemies = pygame.sprite.Group()
for _ in range(5):
    enemy_car = EnemyCar()
    enemies.add(enemy_car)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player_car)
all_sprites.add(enemies)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions between player car and enemy cars
    hits = pygame.sprite.spritecollide(player_car, enemies, False)
    if hits:
        running = False  # Game over if collision occurs

    # Render
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
