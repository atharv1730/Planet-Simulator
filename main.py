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
        
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        if other.sun:
            self.distance_from_sun = distance
            
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        
        for planet in planets:
            if planet == self:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
            
        # Update velocities based on the forces
        self.x_velocity += total_fx / self.mass * self.TIMESTEP
        self.y_velocity += total_fy / self.mass * self.TIMESTEP
        
        # Update position based on the velocities
        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP
        
        # Store the orbit path
        if not self.sun:
            self.orbit.append((self.x, self.y))


def main():
    run = True
    # Used to control the frame rate
    clock = pygame.time.Clock()
    
    sun = Planet(0, 0, 30, (255, 255, 0), 1.98892e30)  # Sun
    sun.sun = True
    
    earth = Planet(-1 * Planet.AU, 0, 16, (0, 0, 255), 5.9742e24)  # Earth

    mars = Planet(-1.524 * Planet.AU, 0, 12, (255, 0, 0), 6.39e23)  # Mars 
    
    mercury = Planet(0.387 * Planet.AU, 0, 8, (150, 150, 150), 3.30e23)  # Mercury
    
    venus = Planet(0.723 * Planet.AU, 0, 14, (255, 165, 50), 4.8685e24)  # Venus
        
    planets = [sun, earth, mars, mercury, venus]
    
    while run:
        clock.tick(60)  # Limit to 60 frames per second
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(win)
        pygame.display.update()

    
    pygame.quit()
    
main()