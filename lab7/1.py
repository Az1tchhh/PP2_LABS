import pygame
##########
import os
w_d = os.getcwd()
##########
pygame.init()
game_display = pygame.display.set_mode((700,618))
pygame.display.set_caption("Ayazhan - TOP!")
clock = pygame.time.Clock()
clock_image = pygame.image.load(os.path.join(w_d, "mickeyclock.png"))
clock_long = pygame.image.load(os.path.join(w_d, "longhand.jpg"))
black = (0,0,0)

#################################################
crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    game_display.fill(black)
    game_display.blit(clock_image, (0,0))
    game_display.blit(clock_long, (20, 40))
    pygame.display.update()
    clock.tick(60)
#################################################
pygame.quit()
quit()