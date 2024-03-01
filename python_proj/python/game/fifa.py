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
BLUE = (0, 0, 255)
GOAL_WIDTH = 100

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])

    def update(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction = (-self.direction[0], self.direction[1])
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.direction = (self.direction[0], -self.direction[1])

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FIFA Soccer Game")

# Create players and ball
player1 = Player(RED, WIDTH // 4, HEIGHT // 2)
player2 = Player(BLUE, WIDTH * 3 // 4, HEIGHT // 2)
ball = Ball()

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, ball)

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

    # Check for collisions between players and ball
    if pygame.sprite.collide_rect(player1, ball) or pygame.sprite.collide_rect(player2, ball):
        ball.direction = (-ball.direction[0], -ball.direction[1])

    # Render
    screen.fill(WHITE)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    pygame.draw.rect(screen, WHITE, (WIDTH // 4 - GOAL_WIDTH // 2, 0, GOAL_WIDTH, HEIGHT), 2)
    pygame.draw.rect(screen, WHITE, (WIDTH * 3 // 4 - GOAL_WIDTH // 2, 0, GOAL_WIDTH, HEIGHT), 2)
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
