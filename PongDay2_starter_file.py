#KPL Intro to Coding Final Project
#The Pong code is started but not complete
#Pong in progress - Starting point for class # 7

# Import Modules and Declare Global Variables

import random, sys, time, pygame
from pygame.locals import *


pygame.init() # starts pygame

FPS = 60 # 60 Frames per second
fpsClock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ball_HEIGHT = 25
ball_WIDTH = 25
ball_SPEED = 5

ball_x_speed = ball_SPEED
ball_y_speed = ball_SPEED
score1 = 0 # This is the score for player 1
score2 = 0 # This is the score for player 2


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
PADDLE_WIDTH = 50
PADDLE_HEIGHT = 200
GUTTER = 50
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

def resetBall():
    global ball_x_pos, ball_y_pos
    ball_x_pos = SCREEN_WIDTH//2
    ball_y_pos = SCREEN_HEIGHT//2

# The Main "game" loop

def main():
    global ball_x_pos, ball_y_pos, ball_x_speed, ball_y_speed, FPSCLOCK
    global theballGraphic, score1, score2, Paddle2_y_pos, Paddle1_y_pos

    DISPLAYSURF.fill(BLACK) # Paint the whole screen a certain color
    pygame.draw.line(DISPLAYSURF, WHITE, (SCREEN_WIDTH//2,0),(SCREEN_WIDTH//2,SCREEN_HEIGHT),25)

    ball_x_pos = ball_x_pos + ball_x_speed # Update the ball's x position
    ball_y_pos = ball_y_pos + ball_y_speed # Update the ball's y position

    DISPLAYSURF.blit(theballGraphic, (ball_x_pos, ball_y_pos)) #ball
    DISPLAYSURF.blit(left_paddle, (Paddle1_x_pos, Paddle1_y_pos)) #left paddle
    DISPLAYSURF.blit(right_paddle, (Paddle2_x_pos, Paddle2_y_pos)) #right paddle
    scoreBoard() # Run the scoreboard function


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
        resetBall()


    # Bounce off the left wall
    if ball_x_pos == 0:
        ball_x_speed = - ball_x_speed  #changes horizontal direction
        score2 = score2 + 1
        resetBall()


    pygame.display.update()    # Refreshes the display
    fpsClock.tick(FPS)

    # Check for a QUIT event (such as closing the window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                print("player 2 pressed up")
                Paddle2_y_pos = Paddle2_y_pos - 30
            if event.key == K_DOWN:
                print("player 2 pressed down")
                Paddle2_y_pos = Paddle2_y_pos + 30
            if event.key == K_w:
                print("player 1 pressed up")
                Paddle1_y_pos = Paddle1_y_pos - 30
            if event.key == K_s:
                print("player 1 pressed down")
                Paddle1_y_pos = Paddle1_y_pos + 30
      







while True:
    main()
