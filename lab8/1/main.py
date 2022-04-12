from dis import dis
import pygame
pygame.init()
####
def drawCircle( screen, x, y, color ):
    pygame.draw.circle( screen, color, ( x, y ), 10 )
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
####
drawingrect = 0 ### if you draw, then ==1
clock = pygame.time.Clock()
finished = False
isPressed = False
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
        ###ERASER+RECT###
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for i in range(650,665):
                for j in range(10, 25):
                    if i == x and j == y:
                        color = white
            for i in range(650,665):
                for j in range(50, 65):
                    if i == x and j == y:
                        drawingrect = 1
                    
            isPressed = True 
        ###ERASER###
                          
        if event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        if event.type == pygame.MOUSEMOTION and isPressed == True and drawingrect == 0:         
            (x, y) = pygame.mouse.get_pos()       # returns the position of mouse cursor
            drawCircle( screen, x, y, color )
        if isPressed == True and drawingrect == 1:  
            (x, y) = pygame.mouse.get_pos()
            drawRect(screen,x,y,40,40, color)
            
    pygame.draw.rect(screen, black, (650,1,15,15), 1)
    pygame.draw.rect(screen, color, (650,40,15,15), 1)
    pygame.display.update()
    clock.tick(240)
pygame.quit()