import pygame
pygame.init()
res = w,h = 700,700
square_res = (100,100,500,500)
surface = pygame.display.set_mode(res)
pygame.display.set_caption("azaza")
clock = pygame.time.Clock()
radius = 25
white = (255,255,255)
red = (255, 0, 0)
black = (0,0,0)
surface.fill(white)

pygame.draw.circle(surface, red, (w/2,h/2), radius)
######
finished = False
cntx = 0
cnty = 0
cntx2=0
cnty2=0
while not finished:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if -11 <= cntx2 <= 11 and -11<= cnty2 <= 11:
                if event.key == pygame.K_LEFT and cntx2!=11:
                    cntx+=20
                    cntx2+=1
                    surface.fill(white)
                    pygame.draw.circle(surface, red, (w/2-cntx,h/2-cnty), radius)
                elif event.key == pygame.K_RIGHT and cntx2!=-11:
                    cntx-=20
                    cntx2-=1
                    surface.fill(white)
                    pygame.draw.circle(surface, red, (w/2-cntx,h/2-cnty), radius)
                elif event.key == pygame.K_UP and cnty2!=11:
                    cnty+=20
                    cnty2+=1
                    surface.fill(white)
                    pygame.draw.circle(surface, red, (w/2-cntx,h/2-cnty), radius)    
                elif event.key == pygame.K_DOWN and cnty2!=-11:
                    cnty-=20
                    cnty2-=1
                    surface.fill(white)
                    pygame.draw.circle(surface, red, (w/2-cntx,h/2-cnty), radius)    
    pygame.draw.rect(surface,black, square_res ,5)

    pygame.display.update()
    clock.tick(10)
pygame.quit()
#######