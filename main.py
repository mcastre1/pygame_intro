import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner") # Set title of window
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('red')

while True:
    for event in pygame.event.get(): # Go through all events.
        if event.type == pygame.QUIT: # Listen for quit event.
            pygame.quit() # Call the quit function.
            exit()

    screen.blit(test_surface,(0,0))

    pygame.display.update()  # This updates the screen surface.
    clock.tick(60) # This tells the while loop that it shouldnt run faster than 60 frames per sec.