import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT,K_SPACE)

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Game')


running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))
    surface = pygame.Surface((50, 50))
    surface.fill((0, 0, 0))
    rect = surface.get_rect()
    #screen.blit(surface, (WIDTH/2, HEIGHT/2))
    surf_center = (
    (WIDTH-surface.get_width())/2,
    (HEIGHT-surface.get_height())/2
)

    # Draw surf at the new coordinates
    screen.blit(surface, surf_center)
    
    pygame.display.flip()
    
pygame.quit()



