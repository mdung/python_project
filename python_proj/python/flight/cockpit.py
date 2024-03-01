import tkinter as tk
from tkinter import ttk
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

# Cockpit Parameters
cockpit_length = 10.0
cockpit_width = 5.0
cockpit_height = 3.0

# Pygame Initialization
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -50)

# Cockpit State
cockpit_position = [0.0, 0.0, 0.0]
vibration_intensity = 0.0

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

def draw_cockpit():
    glBegin(GL_QUADS)
    glVertex3f(-cockpit_length / 2, -cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, -cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(-cockpit_length / 2, cockpit_width / 2, -cockpit_height / 2)

    glVertex3f(-cockpit_length / 2, -cockpit_width / 2, cockpit_height / 2)
    glVertex3f(cockpit_length / 2, -cockpit_width / 2, cockpit_height / 2)
    glVertex3f(cockpit_length / 2, cockpit_width / 2, cockpit_height / 2)
    glVertex3f(-cockpit_length / 2, cockpit_width / 2, cockpit_height / 2)

    glVertex3f(-cockpit_length / 2, -cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, -cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, -cockpit_width / 2, cockpit_height / 2)
    glVertex3f(-cockpit_length / 2, -cockpit_width / 2, cockpit_height / 2)

    glVertex3f(-cockpit_length / 2, cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, cockpit_width / 2, cockpit_height / 2)
    glVertex3f(-cockpit_length / 2, cockpit_width / 2, cockpit_height / 2)

    glVertex3f(-cockpit_length / 2, -cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(-cockpit_length / 2, cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(-cockpit_length / 2, cockpit_width / 2, cockpit_height / 2)
    glVertex3f(-cockpit_length / 2, -cockpit_width / 2, cockpit_height / 2)

    glVertex3f(cockpit_length / 2, -cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, cockpit_width / 2, -cockpit_height / 2)
    glVertex3f(cockpit_length / 2, cockpit_width / 2, cockpit_height / 2)
    glVertex3f(cockpit_length / 2, -cockpit_width / 2, cockpit_height / 2)
    glEnd()

def update_cockpit_vibrations():
    global vibration_intensity
    vibration_intensity = random.uniform(-1, 1)

def main():
    global cockpit_position

    root = tk.Tk()
    root.title("Cockpit Simulator")
    root.geometry("400x200")

    def update_simulation():
        update_cockpit_vibrations()
        cockpit_position[0] += vibration_intensity
        cockpit_position[1] += vibration_intensity
        cockpit_position[2] += vibration_intensity

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glTranslatef(0.0, 0.0, -50)

        draw_aircraft()
        glTranslatef(cockpit_position[0], cockpit_position[1], cockpit_position[2])
        draw_cockpit()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
        root.after(1000 // FPS, update_simulation)

    update_simulation()
    root.mainloop()

if __name__ == "__main__":
    main()
