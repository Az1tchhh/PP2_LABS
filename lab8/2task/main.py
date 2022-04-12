import pygame
import random

pygame.init()
###
def Your_score(screen, score):
    value = "Your Score: " + str(score)
    screen.blit(value, [0, 0])
###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

res = w,h = 700,700

screen = pygame.display.set_mode(res)
pygame.display.set_caption("azaza")
clock = pygame.time.Clock()

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(10)
pygame.quit() 