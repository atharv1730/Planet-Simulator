import pygame
import math

# Initialize Pygame
pygame.init()

# Setting up the window
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")


class Planet:
    # Distance of earth from the sun in meters
    AU = 149.6e6 * 1000  # Astronomical Unit in meters
    G = 6.67428e-11  # Gravitational constant in m^3 kg^-1 s^-2
    SCALE = 250 / AU  # 1 AU = 100 pixels
    TIMESTEP = 3600 * 24  # One day
    
    
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.sun = False
        self.distance_from_sun = 0
        self.orbit = []
        
        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)



def main():
    run = True
    # Used to control the frame rate
    clock = pygame.time.Clock()
    
    sun = Planet(0, 0, 30, (255, 255, 0), 1.98892e30)  # Sun
    sun.sun = True
    
    earth = Planet(-1 * Planet.AU, 0, 16, (0, 0, 255), 5.9742e24)  # Earth
    
        
    planets = [sun, earth]
    
    while run:
        clock.tick(60)  # Limit to 60 frames per second
        
        # win.fill((255, 255, 255))
        # pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(win)
        pygame.display.update()

    
    pygame.quit()
    
main()