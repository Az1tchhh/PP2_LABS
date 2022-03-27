from time import time
import pygame
from datetime import datetime, timedelta
import math
import time

res = w, h = 700, 618
w_half, h_half = w // 2, h // 2
radius_list = {'sec': 300, 'min': 220, 'hour': 150}

pygame.init()
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds

img = pygame.image.load('mickeyclock.png')
img1 = pygame.image.load('longhandpng.png')
img2 = pygame.image.load('shorthandpng.png')

def get_clock_pos_minute(clock_dict, minute, key):
    x = w_half + radius_list[key] * math.cos(math.radians(clock_dict[minute]) - math.pi / 2)
    y = h_half + radius_list[key] * math.sin(math.radians(clock_dict[minute]) - math.pi / 2)
    img12 = pygame.transform.rotate(img1 , -(clock_dict[minute]-90))    
    surface.blit(img12, (w_half - int(img12.get_width() / 2), h_half - int(img12.get_height() / 2)))
    return x, y
def get_clock_pos_hour(clock_dict, hour, key):
    x = w_half + radius_list[key] * math.cos(math.radians(clock_dict[hour]) - math.pi / 2)
    y = h_half + radius_list[key] * math.sin(math.radians(clock_dict[hour]) - math.pi / 2)
    img12 = pygame.transform.rotate(img2 , -(clock_dict[hour]-270))    
    surface.blit(img12, (w_half - int(img12.get_width() / 2), h_half - int(img12.get_height() / 2)))
    return x,y

a=0
cnt=0
while True:
    
    mx, my = w_half, h_half
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
    
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
   
    
    surface.blit(img, (0, 0))
    
    

    
    get_clock_pos_hour(clock60, hour, 'hour')
    get_clock_pos_minute(clock60, minute, 'min')


    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('B Azamat', True, 'white', 'lightblue')
    textRect = text.get_rect()
    textRect.centerx = surface.get_rect().centerx
    textRect.centery = surface.get_rect().centery
    surface.blit(text, textRect)
    pygame.display.flip()
    clock.tick(20)
