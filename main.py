import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner") # Set title of window
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50) # Creating a font for displaying text on the screen.

# This is for making a rectangle only
#test_surface = pygame.Surface((100,200))
# This is for an image import
sky_surface = pygame.image.load("sprites/Sky.png")
ground_surface = pygame.image.load("sprites/ground.png")
text_surface = test_font.render("My game",False,"Green") # Creating the text surface

snail_surface = pygame.image.load('sprites/snail/snail1.png')
snail_x_pos = 600

#test_surface.fill('red')

while True:
    for event in pygame.event.get(): # Go through all events.
        if event.type == pygame.QUIT: # Listen for quit event.
            pygame.quit() # Call the quit function.
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(snail_surface,(snail_x_pos,265))
    snail_x_pos -= 4
    if snail_x_pos <= 0 - snail_surface.get_width():
        snail_x_pos = 800

    pygame.display.update()  # This updates the screen surface.
    clock.tick(60) # This tells the while loop that it shouldnt run faster than 60 frames per sec.