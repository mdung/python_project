import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Rocket parameters
rocket_width = 20
rocket_height = 40
rocket_speed = 5
rocket_angle_change = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Launch Simulator")

# Load images
background_image = pygame.image.load("background.jpg")  # Replace with your background image path
rocket_image = pygame.image.load("rocket.png")  # Replace with your rocket image path

# Rocket class
class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.rotate(rocket_image, 270)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = -90
        self.speed = 0
        self.thrust = False

    def update(self):
        if self.thrust:
            self.speed += 0.2
            self.rect.x += self.speed * math.cos(math.radians(self.angle))
            self.rect.y += self.speed * math.sin(math.radians(self.angle))
            self.speed -= GRAVITY
        else:
            self.speed -= GRAVITY
            self.rect.x += self.speed * math.cos(math.radians(self.angle))
            self.rect.y += self.speed * math.sin(math.radians(self.angle))

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed = 0

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        self.image = pygame.transform.rotate(rocket_image, self.angle)

# Create rocket
rocket = Rocket(WIDTH // 2, HEIGHT - 50)
all_sprites = pygame.sprite.Group()
all_sprites.add(rocket)

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rocket.thrust = True
            elif event.key == pygame.K_LEFT:
                rocket.angle += rocket_angle_change
            elif event.key == pygame.K_RIGHT:
                rocket.angle -= rocket_angle_change
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                rocket.thrust = False

    # Update
    all_sprites.update()

    # Draw
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
