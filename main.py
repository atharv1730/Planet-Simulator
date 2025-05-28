import pygame
import math

# Initialize Pygame
pygame.init()

# Setting up the window
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")


class Planet:
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
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



def main():
    run = True
    # Used to control the frame rate
    clock = pygame.time.Clock()
    
    
    while run:
        clock.tick(60)  # Limit to 60 frames per second
        
        # win.fill((255, 255, 255))
        # pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    
    pygame.quit()
    
main()