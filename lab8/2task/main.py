import pygame
import random
import time

pygame.init()
###

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

score = 0

snake_pos = [50,50]
snake_body = [[100,50], [85,50], [70,50]]
fruit_pos = [random.randrange(1, (w//10)) * 15, 
            random.randrange(1, (h//10)) * 15]
fruit = True
startingdirection = 'right'
direction = startingdirection
finished = False
fruit_spawn = True
while not finished:
    basicFontForText = pygame.font.SysFont(None, 30)
    score_surface = basicFontForText.render('Score : ' + str(score), True, WHITE)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            if event.key == pygame.K_LEFT:
                direction = 'left'
            if event.key == pygame.K_UP:
                direction = 'up'
            if event.key == pygame.K_DOWN:
                direction = 'down'
    if direction == 'up' and startingdirection != 'down':
        startingdirection == 'up'
    if direction == 'down' and startingdirection != 'up':
        startingdirection == 'down'
    if direction == 'right' and startingdirection != 'left':
        startingdirection == 'right'
    if direction == 'left' and startingdirection != 'right':
        startingdirection == 'left'
    
    if startingdirection == 'up':
        snake_pos[1] -= 15
    if startingdirection == 'down':
        snake_pos[1] += 15
    if startingdirection == 'right':
        snake_pos[0] += 15
    if startingdirection == 'down':
        snake_pos[0] -= 15
    
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (w//10)) * 15,
                    random.randrange(1, (h//10)) * 15]
    fruit_spawn = True
    screen.fill(BLACK)
    for pos in range(len(snake_body)):
        pygame.draw.circle(screen, GREEN, (snake_body[pos][0], snake_body[pos][1]), 7.5)
    pygame.draw.circle(screen, WHITE, (fruit_pos[0], fruit_pos[1]), 7.5)

    
    if snake_pos[0] < 0 or snake_pos[0] > w-15:
        time.sleep(3)
        pygame.quit()
    if snake_pos[1] < 0 or snake_pos[1] > h-15:
        time.sleep(3)
        pygame.quit()
    
    pygame.display.update()
    clock.tick(10)
pygame.quit() 