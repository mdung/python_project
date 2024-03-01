import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
RABBIT_SIZE = 20
WOLF_SIZE = 30

# Classes
class Rabbit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((RABBIT_SIZE, RABBIT_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - RABBIT_SIZE)
        self.rect.y = random.randrange(HEIGHT - RABBIT_SIZE)

    def update(self):
        pass

class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WOLF_SIZE, WOLF_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - WOLF_SIZE)
        self.rect.y = random.randrange(HEIGHT - WOLF_SIZE)

    def update(self):
        pass

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ecosystem Simulation")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
rabbits = pygame.sprite.Group()
wolves = pygame.sprite.Group()

# Create initial creatures
for _ in range(10):
    rabbit = Rabbit()
    all_sprites.add(rabbit)
    rabbits.add(rabbit)

for _ in range(3):
    wolf = Wolf()
    all_sprites.add(wolf)
    wolves.add(wolf)

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Render
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Check for interactions (e.g., wolves eating rabbits)
    hits = pygame.sprite.groupcollide(wolves, rabbits, False, True)
    for wolf, eaten_rabbits in hits.items():
        for rabbit in eaten_rabbits:
            new_rabbit = Rabbit()
            all_sprites.add(new_rabbit)
            rabbits.add(new_rabbit)

    # Refresh display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
