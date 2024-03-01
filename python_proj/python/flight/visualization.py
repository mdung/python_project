import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Aircraft Parameters
aircraft_length = 20.0
aircraft_width = 5.0
aircraft_height = 3.0

# Initial State
position = [0.0, 0.0, 0.0]
rotation = [0.0, 0.0, 0.0]

# Pygame Initialization
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -50)

def draw_aircraft():
    glBegin(GL_QUADS)
    glVertex3f(-aircraft_length / 2, -aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, -aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(-aircraft_length / 2, aircraft_width / 2, -aircraft_height / 2)

    glVertex3f(-aircraft_length / 2, -aircraft_width / 2, aircraft_height / 2)
    glVertex3f(aircraft_length / 2, -aircraft_width / 2, aircraft_height / 2)
    glVertex3f(aircraft_length / 2, aircraft_width / 2, aircraft_height / 2)
    glVertex3f(-aircraft_length / 2, aircraft_width / 2, aircraft_height / 2)

    glVertex3f(-aircraft_length / 2, -aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, -aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, -aircraft_width / 2, aircraft_height / 2)
    glVertex3f(-aircraft_length / 2, -aircraft_width / 2, aircraft_height / 2)

    glVertex3f(-aircraft_length / 2, aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, aircraft_width / 2, aircraft_height / 2)
    glVertex3f(-aircraft_length / 2, aircraft_width / 2, aircraft_height / 2)

    glVertex3f(-aircraft_length / 2, -aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(-aircraft_length / 2, aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(-aircraft_length / 2, aircraft_width / 2, aircraft_height / 2)
    glVertex3f(-aircraft_length / 2, -aircraft_width / 2, aircraft_height / 2)

    glVertex3f(aircraft_length / 2, -aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, aircraft_width / 2, -aircraft_height / 2)
    glVertex3f(aircraft_length / 2, aircraft_width / 2, aircraft_height / 2)
    glVertex3f(aircraft_length / 2, -aircraft_width / 2, aircraft_height / 2)
    glEnd()

def main():
    global position, rotation

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rotation[1] += 1
        if keys[pygame.K_RIGHT]:
            rotation[1] -= 1
        if keys[pygame.K_UP]:
            rotation[0] += 1
        if keys[pygame.K_DOWN]:
            rotation[0] -= 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)

        draw_aircraft()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
