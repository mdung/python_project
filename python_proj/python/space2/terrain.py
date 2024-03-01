import pygame
from OpenGL.raw.GL.VERSION.GL_1_0 import glOrtho, glTranslatef, glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from noise import snoise3
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
TERRAIN_SIZE = 100
SCALE = 20
OCTAVES = 6
PERSISTENCE = 0.5
LACUNARITY = 2.0

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

class TerrainGenerator:
    def __init__(self):
        self.terrain = self.generate_terrain()

    def generate_terrain(self):
        terrain = []
        for i in range(TERRAIN_SIZE):
            row = []
            for j in range(TERRAIN_SIZE):
                value = snoise3(
                    i / SCALE,
                    j / SCALE,
                    0,
                    octaves=OCTAVES,
                    persistence=PERSISTENCE,
                    lacunarity=LACUNARITY,
                    )
                row.append(value)
            terrain.append(row)
        return terrain

def draw_terrain(surface, terrain_gen):
    for i in range(TERRAIN_SIZE - 1):
        for j in range(TERRAIN_SIZE - 1):
            vertices = [
                (i * SCALE, j * SCALE, terrain_gen.terrain[i][j] * SCALE),
                ((i + 1) * SCALE, j * SCALE, terrain_gen.terrain[i + 1][j] * SCALE),
                (i * SCALE, (j + 1) * SCALE, terrain_gen.terrain[i][j + 1] * SCALE),
                ((i + 1) * SCALE, (j + 1) * SCALE, terrain_gen.terrain[i + 1][j + 1] * SCALE),
            ]
            pygame.draw.polygon(surface, BROWN, vertices, 0)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Terrain Generator")

    glOrtho(0, WIDTH, HEIGHT, 0, -500, 500)
    gluPerspective(45, (WIDTH / HEIGHT), 0.1, 500.0)
    glTranslatef(WIDTH / 2, HEIGHT / 2, -200)

    terrain_gen = TerrainGenerator()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_terrain(screen, terrain_gen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
