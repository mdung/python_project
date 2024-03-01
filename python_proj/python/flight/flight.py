import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Aircraft Parameters
aircraft_mass = 1000.0  # kg
gravity = 9.81  # m/s^2
thrust_force = 5000.0  # N
drag_coefficient = 0.1
lift_coefficient = 0.1

# Initial State
position = [WIDTH // 2, HEIGHT // 2]
velocity = [0.0, 0.0]
angle = 0.0
angular_velocity = 0.0

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def update_aircraft():
    global position, velocity, angle, angular_velocity

    # Thrust force
    thrust = thrust_force

    # Drag force
    speed = math.sqrt(velocity[0] ** 2 + velocity[1] ** 2)
    drag_force = -drag_coefficient * speed

    # Lift force (for simplicity, using a constant lift coefficient)
    lift_force = lift_coefficient * speed

    # Gravity force
    gravity_force = aircraft_mass * gravity

    # Forces and accelerations
    fx = thrust * math.cos(angle) + drag_force * math.cos(angle) - lift_force * math.sin(angle)
    fy = thrust * math.sin(angle) + drag_force * math.sin(angle) + lift_force * math.cos(angle) - gravity_force

    ax = fx / aircraft_mass
    ay = fy / aircraft_mass

    # Update position and velocity
    position[0] += velocity[0] * 1 / FPS
    position[1] += velocity[1] * 1 / FPS
    velocity[0] += ax * 1 / FPS
    velocity[1] += ay * 1 / FPS

    # Update angle and angular velocity
    angle += angular_velocity * 1 / FPS
    angular_velocity += 0.01 * thrust / aircraft_mass  # Simplified angular acceleration

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
