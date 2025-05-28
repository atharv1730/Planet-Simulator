import pygame
import math

# Initialize Pygame
pygame.init()

# Setting up the window
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")


def main():
    run = True
    # Used to control the frame rate
    clock = pygame.time.Clock()
    
    
    while run:
        clock.tick(60)  # Limit to 60 frames per second
        
        win.fill((255, 255, 255))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    
    pygame.quit()
    
main()