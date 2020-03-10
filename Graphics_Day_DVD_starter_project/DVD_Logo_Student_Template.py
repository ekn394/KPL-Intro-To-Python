#Complete the following DVD Screensaver Code
#The code is started but not complete
#Feb 26, 2019 - Python Day 7

# Import Modules and Declare Global Variables

import random, sys, time, pygame
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LOGO_HEIGHT = 120
LOGO_WIDTH = 200
LOGO_SPEED = 1
Logo_x_speed = LOGO_SPEED
Logo_y_speed = LOGO_SPEED


# Set up colors for future use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Starting position of the Ball
Logo_x_pos = SCREEN_WIDTH/2
Logo_y_pos = SCREEN_HEIGHT/2


# Load the graphics
theLogoGraphic = pygame.image.load('200_118_DVD_Logo_B.png')


# Set up the Game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DVD Screensaveer 97 In Progress") #This is the title




# The Main "game" loop

def main():
    global Logo_x_pos, Logo_y_pos, Logo_x_speed, Logo_y_speed

    DISPLAYSURF.fill(BLACK) # Paint the whole screen a certain color

    Logo_x_pos = Logo_x_pos + Logo_x_speed # Update the Logo's x position
    Logo_y_pos = Logo_y_pos + Logo_y_speed # Update the Logo's y position

    DISPLAYSURF.blit(theLogoGraphic, (Logo_x_pos, Logo_y_pos))

    # Bounce off the ceiling


    # Bounce off the floor


    # Bounce off the right wall


    # Bounce off the left wall


    pygame.display.update()    # Refreshes the display
    fpsClock.tick(FPS)

    # Check for a QUIT event (such as closing the window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

while True:
    main()
