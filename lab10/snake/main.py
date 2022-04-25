import pygame
import random
import psycopg2
import time

conn = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="Mazayka2003",
  host="localhost")


name = input('Enter your name...\n')
sql2 = f'select name, score, level from players where name = \'{name}\''
cursor2 = conn.cursor()
cursor2.execute(sql2)
players2 = cursor2.fetchall()
print(players2)
if len(players2) == 0:
  	print('please register in the system')
else:
	print(f'Your Score: {players2[0][1]}, Your level: {players2[0][2]}')



pygame.init()

snake_speed = 10
res = w,h = 700,700
black = (0, 0, 0)
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.display.set_caption('AZAZAZ')
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

snake_pos = [50, 50]
snake_body = [[50, 50],[40, 50]]
fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
fruit_spawn = True

startdir = 'RIGHT'
direct = startdir
time = 0
def pause(paused):
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			paused = False
		pygame.display.update()
		clock.tick(15)
def Score(score, level, weight):
    basicfont = pygame.font.SysFont(None, 30)
    score_surface = basicfont.render('Your Score : ' + str(score), True, white)
    score_surface2 = basicfont.render('Your Level : ' + str(level), True, white)
    score_surface3 = basicfont.render('Weight : ' + str(weight), True, white)
    screen.blit(score_surface, (0,0))
    screen.blit(score_surface2, (200,0))
    screen.blit(score_surface3, (400,0))
score = 0
basicFontForText = pygame.font.SysFont(None, 30)
cnt=0
kk=0
finished = False
lll = 0
cntxy = 0
pause = 0
while not finished:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				paused = 1
				while paused == 1:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							exit()
					keys = pygame.key.get_pressed()
					if keys[pygame.K_RETURN]:
						paused = 0
					pygame.display.update()
					clock.tick(15)
			if event.key == pygame.K_UP:
				direct = 'UP'
			if event.key == pygame.K_DOWN:
				direct = 'DOWN'
			if event.key == pygame.K_LEFT:
				direct = 'LEFT'
			if event.key == pygame.K_RIGHT:
				direct = 'RIGHT'

	if direct == 'UP' and startdir != 'DOWN':
		startdir = 'UP'
	if direct == 'DOWN' and startdir != 'UP':
		startdir = 'DOWN'
	if direct == 'LEFT' and startdir != 'RIGHT':
		startdir = 'LEFT'
	if direct == 'RIGHT' and startdir != 'LEFT':
		startdir = 'RIGHT'

	
	if startdir == 'UP':
		snake_pos[1] -= 10
	if startdir == 'DOWN':
		snake_pos[1] += 10
	if startdir == 'LEFT':
		snake_pos[0] -= 10
	if startdir == 'RIGHT':
		snake_pos[0] += 10
		
	snake_body.insert(0, list(snake_pos)) #add [0]
	if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
		score += 1
		kk += random.randint(1,5)
		cnt+=1
		fruit_spawn = False
	else:
		snake_body.pop() #delete [last]
	screen.fill(black)#как бы элемент удалился в коде, но не в дисплее,   
					  #чтобы исчезли, заливаем черным)
	if not fruit_spawn:
		fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]	
	fruit_spawn = True
	
	for pos in range(len(snake_body)):
		if pos == 0:
			pygame.draw.circle(screen, RED, (snake_body[pos][0], snake_body[pos][1]), 7.5)
		else:
			pygame.draw.circle(screen, GREEN, (snake_body[pos][0], snake_body[pos][1]), 7.5)
	pygame.draw.circle(screen, white, (fruit_pos[0], fruit_pos[1]), 7.5)

	
	if snake_pos[0] < 0 or snake_pos[0] > w-7.5:
		exit()
	if snake_pos[1] < 0 or snake_pos[1] > h-7.5:
		exit()
	
	if cnt>=3:
		snake_speed+=3
		lll+=1
		cnt=0
	Score(score, lll, kk)

	
	cursor = conn.cursor()
	
	cursor.execute(f'''
	update players
	set score = {score}
	where name = \'{name}\';
	''')
	cursor.execute(f'''
	update players
	set level = {lll}
	where name = \'{name}\';
	''')
	conn.commit()
	cursor.close()

	pygame.display.update()
	clock.tick(snake_speed)