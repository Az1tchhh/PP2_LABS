from dis import dis
import pygame
pygame.init()
####
def drawCircle( screen, x, y, r, color ):
    pygame.draw.circle( screen, color, ( x, y ), r )
def drawRect ( screen, x,y,a,b, color):
    pygame.draw.rect(screen, color, (x,y,a,b))
####
res = w,h = 700,700
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Azaza")

####
white = (255,255,255)
black = (0,0,0)
screen.fill(white)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color = BLUE
List = [RED,GREEN,BLUE]
####
drawingrect = 0 ### if you draw, then ==1
drawingcircle = 0
clock = pygame.time.Clock()
finished = False
isPressed = False
cnt = 0
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_r]:
            color = RED
        elif pressed_keys[pygame.K_g]:
            color = GREEN
        elif pressed_keys[pygame.K_b]:
            color = BLUE
        elif pressed_keys[pygame.K_SPACE]:
            drawingrect = 1
            drawingcircle = 0
        elif pressed_keys[pygame.K_c]:
            drawingcircle = 1
            drawingrect = 0
        ###ERASER+RECT###
        if event.type == pygame.MOUSEBUTTONDOWN:
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
                        color = white
            isPressed = True 
        ###ERASER###
         
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        if event.type == pygame.MOUSEMOTION and isPressed == True and drawingrect == drawingcircle == 0:         
            (x, y) = pygame.mouse.get_pos()   # returns the position of mouse cursor
            if color == white:
                drawRect(screen,x-20,y-20,40,40, color)
            else:
                drawCircle( screen, x, y, 10, color )
        if isPressed == True and drawingrect == 1:  
            (x, y) = pygame.mouse.get_pos()
            drawRect(screen,x-25,y-20,50,40, color)
            drawingrect = 0
        elif isPressed == True and drawingcircle == 1:  
            (x, y) = pygame.mouse.get_pos()
            drawCircle( screen, x, y, 20, color )
            drawingcircle = 0
    pygame.draw.rect(screen, black, (650,1,15,15), 1)
    pygame.draw.rect(screen, color, (650,40,15,15))
    pygame.display.update()
    clock.tick(240)
pygame.quit()