import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Map variables
map_size = (10, 10)  # Adjust the size of the map grid
tile_size = 1.0

def draw_map():
    for x in range(map_size[0]):
        for y in range(map_size[1]):
            draw_tile(x, y)

def draw_tile(x, y):
    glPushMatrix()
    glTranslatef(x * tile_size, y * tile_size, 0)

    # Draw a simple square as a placeholder for a map tile
    glBegin(GL_QUADS)
    glVertex3f(0, 0, 0)
    glVertex3f(tile_size, 0, 0)
    glVertex3f(tile_size, tile_size, 0)
    glVertex3f(0, tile_size, 0)
    glEnd()

    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-map_size[0] * tile_size / 2, -map_size[1] * tile_size / 2, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the 3D map
        draw_map()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
