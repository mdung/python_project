import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Set up Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Player variables
player_x, player_y, player_z = 0, 0, 0
player_speed = 0.1

# Martian environment variables
mars_color = (1, 0.5, 0)  # Martian surface color

def draw_mars():
    glColor3fv(mars_color)
    glutSolidSphere(1, 50, 50)  # Draw a simple sphere as the Martian surface

def draw_player():
    glPushMatrix()
    glTranslatef(player_x, player_y, player_z)
    glColor3f(0, 0, 1)  # Blue color for the player
    glutSolidCube(0.2)  # Draw a simple cube as the player
    glPopMatrix()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= player_speed
    if keys[K_RIGHT]:
        player_x += player_speed
    if keys[K_UP]:
        player_z += player_speed
    if keys[K_DOWN]:
        player_z -= player_speed

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the Martian environment
    draw_mars()

    # Draw the player
    draw_player()

    pygame.display.flip()
    pygame.time.wait(10)
