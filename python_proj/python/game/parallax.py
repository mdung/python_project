import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 255, 255)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

# Background class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_path, y_pos):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.y = y_pos

    def update(self):
        self.rect.y += 5  # Scroll speed

        # Reset position when the image moves off the screen
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Effect with Pygame")

# Create player
player = Player()

# Create background layers
background_layers = [
    Background("background_layer1.png", 0),
    Background("background_layer2.png", -HEIGHT),
]

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(background_layers)

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
    screen.fill(BG_COLOR)
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
