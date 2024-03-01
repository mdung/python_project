import pygame
import sys
from pygame.locals import *
from math import radians, sin, cos

# Constants for the solar system
SUN_RADIUS = 50
EARTH_RADIUS = 10
MARS_RADIUS = 8
VENUS_RADIUS = 12
MERCURY_RADIUS = 8

ORBIT_RADIUS_EARTH = 200
ORBIT_RADIUS_MARS = 300
ORBIT_RADIUS_VENUS = 150
ORBIT_RADIUS_MERCURY = 100

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (169, 169, 169)

class SolarSystem:
    def __init__(self):
        self.width, self.height = 800, 600
        self.center = (self.width // 2, self.height // 2)
        self.clock = pygame.time.Clock()

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Solar System Simulator")

        self.sun = self.create_planet(SUN_RADIUS, YELLOW, self.center)
        self.earth_orbit = self.create_orbit(ORBIT_RADIUS_EARTH, GRAY, self.center)
        self.earth = self.create_planet(EARTH_RADIUS, BLUE, (self.center[0] + ORBIT_RADIUS_EARTH, self.center[1]))

        self.mars_orbit = self.create_orbit(ORBIT_RADIUS_MARS, GRAY, self.center)
        self.mars = self.create_planet(MARS_RADIUS, RED, (self.center[0] + ORBIT_RADIUS_MARS, self.center[1]))

        self.venus_orbit = self.create_orbit(ORBIT_RADIUS_VENUS, GRAY, self.center)
        self.venus = self.create_planet(VENUS_RADIUS, (255, 165, 0), (self.center[0] + ORBIT_RADIUS_VENUS, self.center[1]))

        self.mercury_orbit = self.create_orbit(ORBIT_RADIUS_MERCURY, GRAY, self.center)
        self.mercury = self.create_planet(MERCURY_RADIUS, (184, 134, 11), (self.center[0] + ORBIT_RADIUS_MERCURY, self.center[1]))

    def create_planet(self, radius, color, position):
        return {
            "radius": radius,
            "color": color,
            "position": position,
            "angle": 0,
            "angular_speed": 0.02  # Adjust the speed for each planet
        }

    def create_orbit(self, radius, color, center):
        return {
            "radius": radius,
            "color": color,
            "center": center
        }

    def update_planet_position(self, planet):
        planet["angle"] += planet["angular_speed"]
        x = int(planet["center"][0] + planet["radius"] * cos(planet["angle"]))
        y = int(planet["center"][1] + planet["radius"] * sin(planet["angle"]))
        return x, y

    def run_simulation(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(WHITE)

            self.draw_orbit(self.earth_orbit)
            self.draw_planet(self.earth)

            self.draw_orbit(self.mars_orbit)
            self.draw_planet(self.mars)

            self.draw_orbit(self.venus_orbit)
            self.draw_planet(self.venus)

            self.draw_orbit(self.mercury_orbit)
            self.draw_planet(self.mercury)

            pygame.display.flip()
            self.clock.tick(60)

            # Update planet positions
            self.earth["position"] = self.update_planet_position(self.earth)
            self.mars["position"] = self.update_planet_position(self.mars)
            self.venus["position"] = self.update_planet_position(self.venus)
            self.mercury["position"] = self.update_planet_position(self.mercury)

    def draw_planet(self, planet):
        pygame.draw.circle(self.screen, planet["color"], planet["position"], planet["radius"])

    def draw_orbit(self, orbit):
        pygame.draw.circle(self.screen, orbit["color"], orbit["center"], orbit["radius"], 1)

if __name__ == "__main__":
    solar_system = SolarSystem()
    solar_system.run_simulation()
