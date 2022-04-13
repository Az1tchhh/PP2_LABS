#Imports
from turtle import back
from winreg import EnableReflectionKey
import pygame, sys
from pygame.locals import *
import random, time
#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("road.png")
background = pygame.transform.rotate(background, -90)
background = pygame.transform.scale(background, (400,600))
machine = pygame.image.load("Player.png")
#Create a white screen 
screen = pygame.display.set_mode((400,600))

pygame.display.set_caption("Game")

startpoint = [200,500]
screen.blit(background, (0,0))
change_to = 'RIGHT'
cnt=0
#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    if -11 <= cnt <= 8:
        if change_to == 'RIGHT' and cnt!=8:
            startpoint[0] += 20
            cnt +=1
            change_to = 'UP'
        if change_to == 'LEFT' and cnt!=-11:
            startpoint[0] -= 20
            cnt -=1
            change_to = 'UP'
    screen.blit(background, (0,0))
    screen.blit(machine, (startpoint[0],startpoint[1]))
    

    pygame.display.flip()
    FramePerSec.tick(FPS)