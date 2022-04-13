from tracemalloc import start
import pygame
import random


pygame.init()
###
snake_speed = 10
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

snake_pos = [100,50]
snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]
fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
fruit = True

startdir = 'RIGHT'
change_to = startdir

finished = False
fruit_spawn = True
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#2
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
    if change_to == 'UP' and startdir != 'DOWN':
		startdir = 'UP'
	if change_to == 'DOWN' and startdir != 'UP':
		startdir = 'DOWN'
	if change_to == 'LEFT' and startdir != 'RIGHT':
		startdir = 'LEFT'
	if change_to == 'RIGHT' and startdir != 'LEFT':
		startdir = 'RIGHT'

	
	if startdir == 'UP':
		snake_pos[1] -= 10
	if startdir == 'DOWN':
		snake_position[1] += 10
	if startdir == 'LEFT':
		snake_position[0] -= 10
	if startdir == 'RIGHT':
		snake_position[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
    fruit_spawn = True
    screen.fill(BLACK)
    for pos in range(len(snake_body)):
        pygame.draw.circle(screen, GREEN, (snake_body[pos][0], snake_body[pos][1]), 7.5)
    pygame.draw.circle(screen, WHITE, (fruit_pos[0], fruit_pos[1]), 7.5)

    
    if snake_pos[0] < 0 or snake_pos[0] > w-15:
        exit()
    if snake_pos[1] < 0 or snake_pos[1] > h-15:
        exit()
    basicFontForText = pygame.font.SysFont(None, 30)
    text = basicFontForText.render('B Azamat', True, 'grey', 'white')
    surface.blit(text, (0,0))
    pygame.display.update()
    clock.tick(snake_speed)
pygame.quit() 