import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load(f"image/frame_{i}.png") for i in range(1, 9)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.animation_speed = 5
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter % self.animation_speed == 0:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Sprites in Python Game")

# Create player
player = Player()

# Create sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

    # Render
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
