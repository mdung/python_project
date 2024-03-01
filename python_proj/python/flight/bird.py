import random
import math
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

# Bird Parameters
bird_size = 1.0
bird_speed = 2.0
bird_flock_size = 20

# Pygame Initialization
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -20)

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

def draw_bird(x, y, z):
    glBegin(GL_QUADS)
    glVertex3f(x - bird_size / 2, y - bird_size / 2, z)
    glVertex3f(x + bird_size / 2, y - bird_size / 2, z)
    glVertex3f(x + bird_size / 2, y + bird_size / 2, z)
    glVertex3f(x - bird_size / 2, y + bird_size / 2, z)
    glEnd()

def draw_bird_flock(flock):
    for bird in flock:
        x, y, z = bird['position']
        draw_bird(x, y, z)

def move_bird(bird):
    bird['position'][0] += bird_speed * math.cos(math.radians(bird['angle']))
    bird['position'][1] += bird_speed * math.sin(math.radians(bird['angle']))
    bird['position'][2] += bird_speed * 0.1  # Vertical movement (optional)

def generate_bird_flock():
    flock = []
    for _ in range(bird_flock_size):
        x = random.uniform(-20, 20)
        y = random.uniform(-20, 20)
        z = random.uniform(0, 20)
        angle = random.uniform(0, 360)
        flock.append({'position': [x, y, z], 'angle': angle})
    return flock

def main():
    global scenery_objects

    bird_flock = generate_bird_flock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)

        draw_aircraft()
        draw_bird_flock(bird_flock)

        for bird in bird_flock:
            move_bird(bird)

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
