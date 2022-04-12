import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


res = w,h = 700, 700

screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

game_over = False
color = BLUE
prev, cur = None, None
screen.fill(WHITE)
cnt=0
List = [RED,GREEN,BLUE]
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            x,y = pygame.mouse.get_pos()
            for i in range(650,665):
                for j in range(40, 55):
                    if i == x and j == y:
                        if cnt>2:
                            cnt=0
                        color = List[cnt]
                        cnt+=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for i in range(650,665):
                for j in range(1, 16):
                    if i == x and j == y:
                        color = WHITE
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if prev:
            if color == WHITE:
                pygame.draw.rect(screen, color, (prev, cur, 20, 20), )
            else:
                pygame.draw.line(screen, color, prev, cur, 10)
            prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    
    pygame.draw.rect(screen, BLACK, (650,1,15,15), 1)
    pygame.draw.rect(screen, color, (650,40,15,15))
    pygame.draw.rect(screen, BLACK, (648,38,17,17), 2)
    pygame.display.flip()

    clock.tick(120)


pygame.quit()