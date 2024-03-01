import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Simulation")
clock = pygame.time.Clock()

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2, 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH), y=random.randint(0, HEIGHT))

    def update(self):
        self.rect.x += random.uniform(-1, 1)
        self.rect.y += random.uniform(-1, 1)
        if self.rect.x > WIDTH: self.rect.x = 0
        elif self.rect.x < 0: self.rect.x = WIDTH
        if self.rect.y > HEIGHT: self.rect.y = 0
        elif self.rect.y < 0: self.rect.y = HEIGHT

all_sprites = pygame.sprite.Group()
[all_sprites.add(Star()) for _ in range(100)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
