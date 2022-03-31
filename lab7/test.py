import pygame
pygame.init()
res = w , h = 1000,700
surface = pygame.display.set_mode(res)
pygame.display.set_caption("AZAZZA")
clock = pygame.time.Clock()
finished = False
while not finished:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    clock.tick(15)
            
            