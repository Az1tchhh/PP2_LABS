import pygame
from datetime import datetime, timedelta
import math

RES = WIDTH, HEIGHT = 700, 618
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 20, 'min': RADIUS - 75, 'hour': RADIUS - 120}

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds

img = pygame.image.load('mickeyclock.png')
img1 = pygame.image.load('longhandpng.png')
img2 = pygame.image.load('shorthandpng.png')

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    img12 = pygame.transform.rotate(img1 , a)
    surface.blit(img12, (mx - int(img12.get_width() / 2), my - int(img12.get_height() / 2)))
    return x, y




def longhand(time, clock_dict, clock_hand,a):
    if clock_dict[clock_hand] == time.hour:
        img12 = pygame.transform.rotate(img1 , a)
        surface.blit(img12, (mx - int(img12.get_width() / 2), my - int(img12.get_height() / 2)))

b = datetime.now().minute
if b>15:
    img12 = pygame.transform.rotate(img1 , (b-15)*6)
    
a=0
cnt=0
while True:
    a-=6
    mx, my = H_WIDTH, H_HEIGHT
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
    # set bg
    # get time now
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    # draw face
    
    surface.blit(img, (0, 0))
    # draw clock
    
    img12 = pygame.transform.rotate(img1 , a)
    surface.blit(img12, (mx - int(img12.get_width() / 2), my - int(img12.get_height() / 2)))
    
    pygame.draw.line(surface, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 12)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)


    pygame.display.flip()
    clock.tick(1)
