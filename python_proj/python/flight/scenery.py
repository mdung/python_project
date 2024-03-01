import tkinter as tk
from tkinter import ttk
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Building Parameters
building_width = 5.0
building_height = 10.0

# Scenery Objects
scenery_objects = []

# Pygame Initialization
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -20)

def draw_building(x, y):
    glBegin(GL_QUADS)
    glVertex3f(x - building_width / 2, y - building_width / 2, 0)
    glVertex3f(x + building_width / 2, y - building_width / 2, 0)
    glVertex3f(x + building_width / 2, y + building_width / 2, 0)
    glVertex3f(x - building_width / 2, y + building_width / 2, 0)
    glEnd()

def draw_scenery():
    for obj in scenery_objects:
        x, y = obj['position']
        draw_building(x, y)

def main():
    global scenery_objects

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    x = (x / WIDTH - 0.5) * 40
                    y = (0.5 - y / HEIGHT) * 40
                    scenery_objects.append({'position': [x, y]})

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)

        draw_scenery()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
