
#Pygame Boilerplate

import random, sys, time, pygame
from pygame.locals import *

pygame.init()

FPS = 60  # Frames per second
fpsClock = pygame.time.Clock()  # The clock
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Set up colors for future use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0,128, 0)
DARK_BLUE = (0,0,128)
PURPLE = (128,0,128)
TEAL = (0,128,128)
YELLOW = (255,255,0)

# Set up the Game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("A Title Goes here!") #This is the title

DISPLAYSURF.fill(WHITE) # Paint the whole screen a certain color
pygame.draw.circle(DISPLAYSURF, RED, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 100, 0) 
#pygame.draw.line(DISPLAYSURF, BLACK, (20,20),(40,40),2)



def main():

    pygame.display.update()    # Refreshes the display

    fpsClock.tick(FPS)  # Have the clock tick once

    # Check for a QUIT event (such as closing the window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


while True:
    main()
