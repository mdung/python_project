import pygame
import sys
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Aircraft Parameters
aircraft_length = 20.0
aircraft_width = 5.0
aircraft_height = 3.0

# Initial State
position = [WIDTH // 2, HEIGHT // 2]
velocity = [0.0, 0.0]
angle = 0.0
angular_velocity = 0.0

# Wind Parameters
wind_speed = 10.0
turbulence_intensity = 5.0

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def update_aircraft():
    global position, velocity, angle, angular_velocity

    # Wind effects
    wind_force = [random.uniform(-turbulence_intensity, turbulence_intensity), wind_speed]

    # Apply wind force
    velocity[0] += wind_force[0] * 1 / FPS
    velocity[1] += wind_force[1] * 1 / FPS

    # Update position and velocity
    position[0] += velocity[0] * 1 / FPS
    position[1] += velocity[1] * 1 / FPS

    # Update angle and angular velocity
    angle += angular_velocity * 1 / FPS
    angular_velocity += 0.01 * wind_force[1] / 20  # Simplified angular acceleration

def draw_aircraft():
    aircraft_image = pygame.Surface((50, 30), pygame.SRCALPHA)
    pygame.draw.polygon(aircraft_image, WHITE, [(0, 15), (50, 0), (50, 30)])
    rotated_aircraft = pygame.transform.rotate(aircraft_image, math.degrees(angle))
    rect = rotated_aircraft.get_rect(center=(position[0], position[1]))
    screen.blit(rotated_aircraft, rect.topleft)

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    update_aircraft()
    draw_aircraft()

    pygame.display.flip()
    clock.tick(FPS)
