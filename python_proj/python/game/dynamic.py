import pygame
import pymunk
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Soft-Body Physics")

# Set up Pygame clock
clock = pygame.time.Clock()

# Set up pymunk space
space = pymunk.Space()
space.gravity = 0, -1000  # You can adjust gravity as needed

# Create ground
ground = pymunk.Segment(space.static_body, (0, 50), (width, 50), 5)
ground.friction = 0.5
space.add(ground)

# Create soft-body particles
particles = []
for x in range(100, 700, 20):
    for y in range(300, 500, 20):
        mass = 1
        radius = 5
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment)
        body.position = x, y
        shape = pymunk.Circle(body, radius)
        space.add(body, shape)
        particles.append(shape)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update physics
    space.step(1 / 60.0)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw ground
    pygame.draw.line(screen, (0, 0, 0), ground.a, ground.b, 5)

    # Draw particles
    for particle in particles:
        pos_x, pos_y = map(int, particle.body.position)
        pygame.draw.circle(screen, (0, 0, 255), (pos_x, height - pos_y), int(particle.radius), 2)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
