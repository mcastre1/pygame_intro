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
sky_surface = pygame.image.load("sprites/Sky.png").convert_alpha()  # By using convert it will make the images easier to work with.
ground_surface = pygame.image.load("sprites/ground.png").convert_alpha() # By using convert, our game runs smoother and faster.
text_surface = test_font.render("My game",False,"Green") # Creating the text surface

snail_surface = pygame.image.load('sprites/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomleft = (600, 300))

player_surface = pygame.image.load("sprites/player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(bottomleft=(80,300)) # This is how you make it easier to place an image easier.

#test_surface.fill('red')

while True:
    for event in pygame.event.get(): # Go through all events.
        if event.type == pygame.QUIT: # Listen for quit event.
            pygame.quit() # Call the quit function.
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(snail_surface,snail_rectangle)
    snail_rectangle.left -= 4

    if snail_rectangle.left <= 0 - snail_rectangle.width:
        snail_rectangle.left = 800
    
    screen.blit(player_surface,player_rectangle)

    pygame.display.update()  # This updates the screen surface.
    clock.tick(60) # This tells the while loop that it shouldnt run faster than 60 frames per sec.