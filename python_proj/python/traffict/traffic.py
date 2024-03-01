import pygame
import random
import time

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CAR_RADIUS = 10
MAX_SPEED = 5
MIN_DISTANCE = 30

# Traffic light states
RED = "red"
GREEN = "green"

class Car:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x += self.speed

    def get_position(self):
        return self.x, self.y

class RoadConstructionSite:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_inside(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

class TrafficSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Road Construction Traffic Simulation")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Road Construction Traffic Simulation")
        self.clock = pygame.time.Clock()

        self.cars = [Car(x=random.randint(0, WIDTH), y=random.randint(0, HEIGHT), speed=random.uniform(1, MAX_SPEED)) for _ in range(10)]

        # Create a road construction site
        self.construction_site = RoadConstructionSite(300, 200, 200, 50)

        self.master.after(0, self.update_simulation)

    def update_simulation(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i, car in enumerate(self.cars):
            # Car-following model
            if i > 0:
                leading_car = self.cars[i - 1]
                distance = leading_car.x - car.x
                if distance < MIN_DISTANCE:
                    car.speed = min(car.speed, distance / 2)

            # Check if the car is inside the construction site
            if self.construction_site.is_inside(car.x, car.y):
                car.speed = 0  # Slow down or stop

            car.move()

            # Wrap around the screen
            if car.x > WIDTH:
                car.x = 0

        self.screen.fill((255, 255, 255))

        # Draw road construction site
        pygame.draw.rect(self.screen, (255, 0, 0), (self.construction_site.x, self.construction_site.y, self.construction_site.width, self.construction_site.height))

        for car in self.cars:
            pygame.draw.circle(self.screen, (0, 0, 255), (int(car.x), int(car.y)), CAR_RADIUS)

        pygame.display.flip()
        self.clock.tick(FPS)
        self.master.after(1000 // FPS, self.update_simulation)

if __name__ == "__main__":
    root = pygame.display.set_mode((WIDTH, HEIGHT))
    app = TrafficSimulation(root)
    pygame.display.set_caption("Road Construction Traffic Simulation")
    app.master.mainloop()
