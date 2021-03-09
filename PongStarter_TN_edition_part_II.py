# KPL Intro to Coding Final Project - Winter 2021
# The Pong code is started but not complete
# Pong in progress - Starting point for class # 8
# TODO:
# 1. Enable the scoreboard
# 2. Add points when the ball hits either left or right walls
# 3. Reset the ball to the center whenever a point is scored
# 4. Enable key presses to move the paddles
# 5. Have the ball bounce off of the paddles
# 6. Make a function that changes the trajectory of the ball.
# 7. Add sound effects.
# 8. Have fun!


# Import Modules and Declare Global Variables

import random, sys, time, pygame
from pygame.locals import *


pygame.init()
# GLOBAL VARIABLES 
FPS = 60
fpsClock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ball_HEIGHT = 25 
ball_WIDTH = 25
ball_SPEED = 5
BALL_SIZE = 25
GUTTER = 50
PADDLE_HEIGHT = 200
PADDLE_WIDTH = 50
ball_x_speed = ball_SPEED
ball_y_speed = ball_SPEED
score1 = 0
score2 = 0


# Set up colors for future use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Starting position of the Ball
ball_x_pos = SCREEN_WIDTH//2
ball_y_pos = SCREEN_HEIGHT//2

#Starting position of the Paddles
Paddle1_y_pos = ((SCREEN_HEIGHT//2)-(PADDLE_HEIGHT//2))
Paddle1_x_pos = GUTTER
Paddle2_y_pos = ((SCREEN_HEIGHT//2)-(PADDLE_HEIGHT//2))
Paddle2_x_pos = SCREEN_WIDTH - GUTTER - PADDLE_WIDTH

# Load the graphics
theballGraphic = pygame.image.load('pong_ball_25_cube.png') 
right_paddle = pygame.image.load('pong_paddle.png') 
left_paddle = pygame.image.load('pong_paddle.png') 

# Set up the Game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong in Progress") #This is the title

'''
#Load the Sound effects
pygame.mixer.init(44100, -16, 2, 2048)
beep1 = pygame.mixer.Sound('pongBlip1.ogg')
beep2 = pygame.mixer.Sound('pongBlip2.ogg')
'''


# Helper functions




def scoreBoard():
    RETROFONT = pygame.font.Font('PressStart2P.ttf', 48)
    scoreSurf = RETROFONT.render( str(score1) + '   ' + str(score2), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (SCREEN_WIDTH//3, SCREEN_HEIGHT //5)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def nextRound():
    global ball_x_pos, ball_y_pos
    ball_x_pos = SCREEN_WIDTH//2
    ball_y_pos = SCREEN_HEIGHT//2
    
# The Main "game" loop

def main():
    global ball_x_pos, ball_y_pos, ball_x_speed, ball_y_speed, FPSCLOCK
    global theballGraphic, score1, score2, Paddle2_y_pos, Paddle1_y_pos
    
    DISPLAYSURF.fill(BLACK) # Paint the whole screen a certain color
    scoreBoard()
    pygame.draw.line(DISPLAYSURF, WHITE, (SCREEN_WIDTH//2,0),(SCREEN_WIDTH//2,SCREEN_HEIGHT),25)

    ball_x_pos = ball_x_pos + ball_x_speed # Update the ball's x position
    ball_y_pos = ball_y_pos + ball_y_speed # Update the ball's y position
    
    DISPLAYSURF.blit(theballGraphic, (ball_x_pos, ball_y_pos)) #draw ball
    DISPLAYSURF.blit(left_paddle, (Paddle1_x_pos, Paddle1_y_pos)) #draw left paddle
    DISPLAYSURF.blit(right_paddle, (Paddle2_x_pos, Paddle2_y_pos)) #draw right paddle
    

    # Bounce off the ceiling
    if ball_y_pos == 0:
        ball_y_speed = - ball_y_speed  #changes vertical direction

    # Bounce off the floor
    if ball_y_pos == SCREEN_HEIGHT - ball_HEIGHT:
        ball_y_speed = - ball_y_speed  #changes vertical direction

    # Bounce off the right wall
    if ball_x_pos == SCREEN_WIDTH - ball_WIDTH:
        ball_x_speed = - ball_x_speed  #changes horizontal direction
        score1 = score1 + 1
        nextRound()

    # Bounce off the left wall
    if ball_x_pos == 0:
        ball_x_speed = - ball_x_speed  #changes horizontal direction
        score2 = score2 + 1
        nextRound()

    #Bounce off the left paddle
    if(ball_x_pos == (GUTTER+PADDLE_WIDTH)):
        if ((Paddle1_y_pos - (BALL_SIZE*2//3)) <= ball_y_pos <= (Paddle1_y_pos + PADDLE_HEIGHT - (BALL_SIZE//3))):
            print ("hit the left paddle")

    #Bounce off the right paddle
    if(ball_x_pos == ((SCREEN_WIDTH - GUTTER - PADDLE_WIDTH - BALL_SIZE))):
        if ((Paddle2_y_pos - (BALL_SIZE*2//3)) <= ball_y_pos <= (Paddle2_y_pos + PADDLE_HEIGHT - (BALL_SIZE//3))):
            print ("hit the right paddle")


    pygame.display.update()    # Refreshes the display
    fpsClock.tick(FPS)

    # Check for a QUIT event (such as closing the window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
           
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                print("you pressed up")
                Paddle2_y_pos = Paddle2_y_pos - 30
            if event.key == K_DOWN:
                print("you pressed down")
                Paddle2_y_pos = Paddle2_y_pos + 30
        

	

while True:
    main()
