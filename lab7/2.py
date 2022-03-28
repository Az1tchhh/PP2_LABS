import pygame
pygame.init()
res = w,h = 600, 700
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()
red = (255, 0, 0)
black = (0, 0, 0)
############################################
pygame.draw.circle(surface, black, (130,576), 50, 5)
pygame.draw.lines(surface, black, True, [ [106,577] , [143,552], [143,602]])
############################################
img = pygame.image.load("msg988533202-148907.jpg")
img = pygame.transform.scale(img, (600,700))
first_song = pygame.mixer.music.load('Aquaneon - Сердце Лёд.mp3')
second_song = pygame.mixer.music.load('Artik & Asti - Гармония.mp3')
third_song = pygame.mixer.music.load('Artik & Asti - Девочка, Танцуй.mp3')
surface.blit(img, (0,0))
sound1 = pygame.mixer.Sound('Aquaneon - Сердце Лёд.mp3')
sound2 = pygame.mixer.Sound('Artik & Asti - Гармония.mp3')
sound3 = pygame.mixer.Sound('Artik & Asti - Девочка, Танцуй.mp3')
list = [sound1, sound2, sound3]
#############################################TEXT
basicFont = pygame.font.SysFont(None, 38)
basicFont2 = pygame.font.SysFont(None, 33)
text1 = basicFont.render('Aquaneon - Сердце Лёд', True, 'black', 'white')
text2 = basicFont.render('Artik & Asti - Гармония', True, 'black', 'white')
text3 = basicFont2.render('Artik & Asti - Девочка, Танцуй', True, 'black', 'white')

surface.blit(text1, (142,130))
surface.blit(text2, (150,260))
surface.blit(text3, (134,390))
#############################################
finished= False
cnt=0
tf = 0
seconds = 0
a = list[cnt].get_length()
print(a)
while not finished: 
    if cnt ==0: ##92 98 413 100
        pygame.draw.rect(surface, red, (90,95,417,105), 6)
        pygame.draw.rect(surface, black, (91,221,419,105), 6)
        pygame.draw.rect(surface, black, (90,354,418,105), 6)
    elif cnt == 1:
        pygame.draw.rect(surface, black, (90,95,417,105), 6)
        pygame.draw.rect(surface, red, (91,221,419,105), 6)
        pygame.draw.rect(surface, black, (90,354,418,105), 6)
    else:
        pygame.draw.rect(surface, black, (90,95,417,105), 6)
        pygame.draw.rect(surface, black, (91,221,419,105), 6)
        pygame.draw.rect(surface, red, (90,354,418,105), 6)
    ################################################################################
    pygame.draw.circle(surface, black, (130,576), 50, 5)
    pygame.draw.lines(surface, black, True, [ [106,577] , [143,552], [143,602]], 3)
    ################################################################################
    pygame.draw.circle(surface, black, (w/2-10,576), 50, 5)
    pygame.draw.line(surface, black, [271,552] , [271,595], 3)
    pygame.draw.line(surface, black, [306,552] , [306,595], 3)
    ################################################################################
    pygame.draw.circle(surface, black, (450,576), 50, 5)
    pygame.draw.lines(surface, black, True, [ [474,577] , [437,552], [437,602]], 3)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                list[cnt].stop()
                cnt+=1
                if cnt>len(list)-1:
                    cnt=0
                list[cnt].play()
                tf = 1
            elif event.key == pygame.K_LEFT:
                list[cnt].stop()
                cnt-=1
                if cnt<0:
                    cnt=2
                list[cnt].play()
                tf=1
            elif event.key == pygame.K_SPACE and tf==0:
                list[cnt].play()
                tf = 1
            elif event.key == pygame.K_SPACE and tf==1:
                list[cnt].stop()
                tf = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.draw.circle(surface, red, (130,576), 50, 5)
                pygame.draw.circle(surface, black, (w/2-10,576), 50, 5)
                pygame.draw.circle(surface, black, (450,576), 50, 5)
            elif event.key == pygame.K_RIGHT:
                pygame.draw.circle(surface, black, (130,576), 50, 5)
                pygame.draw.circle(surface, black, (w/2-10,576), 50, 5)
                pygame.draw.circle(surface, red, (450,576), 50, 5)
            elif event.key == pygame.K_SPACE:
                pygame.draw.circle(surface, black, (130,576), 50, 5)
                pygame.draw.circle(surface, red, (w/2-10,576), 50, 5)
                pygame.draw.circle(surface, black, (450,576), 50, 5)
    basicFontForText = pygame.font.SysFont(None, 30)
    text = basicFontForText.render('B Azamat', True, 'grey', 'white')
    surface.blit(text, (0,0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()