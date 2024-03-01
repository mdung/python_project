import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dynamic Vegetation System")

# Set up Pygame clock
clock = pygame.time.Clock()

# Define a class for the vegetation
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.original_angle = random.uniform(0, 360)  # Random initial angle
        self.amplitude = random.uniform(5, 20)  # Random amplitude
        self.frequency = random.uniform(0.02, 0.1)  # Random frequency
        self.color = (34, 139, 34)  # Green color

    def update(self, time_elapsed):
        # Update angle based on time and wind
        wind_force = math.sin(self.frequency * time_elapsed) * self.amplitude
        self.angle = self.original_angle + wind_force

    def draw(self):
        # Draw a simple plant as a line
        length = 50
        end_x = self.x + length * math.cos(math.radians(self.angle))
        end_y = self.y + length * math.sin(math.radians(self.angle))
        pygame.draw.line(screen, self.color, (self.x, self.y), (end_x, end_y), 3)

# Create a list of plants
plants = [Plant(random.randint(50, width - 50), random.randint(50, height - 50)) for _ in range(10)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update wind simulation
    time_elapsed = pygame.time.get_ticks() / 100  # Convert to seconds for smoother animation

    # Clear screen
    screen.fill((255, 255, 255))

    # Update and draw plants
    for plant in plants:
        plant.update(time_elapsed)
        plant.draw()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
