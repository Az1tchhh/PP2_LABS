from time import time
import pygame
from datetime import datetime, timedelta
import math
import time

res = w, h = 700, 618
w_half, h_half = w // 2, h // 2

pygame.init()
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds

img = pygame.image.load('mickeyclock.png')
img1 = pygame.image.load('longhandpng.png')
img2 = pygame.image.load('shorthandpng.png')
def get_clock_pos_seconds(clock_dict, second):
    x = w_half + 200 * math.cos(math.radians(clock_dict[second]) - math.pi/2)
    y = h_half + 200 * math.sin(math.radians(clock_dict[second]) - math.pi/2)
    return x,y
def get_clock_pos_minute(clock_dict, minute, key):
    img12 = pygame.transform.rotate(img1 , -(clock_dict[minute]-90))    
    surface.blit(img12, (w_half - int(img12.get_width() / 2), h_half - int(img12.get_height() / 2)))
    
def get_clock_pos_hour(clock_dict, hour, key):
    img12 = pygame.transform.rotate(img2 , -(clock_dict[hour]-270))    
    surface.blit(img12, (w_half - int(img12.get_width() / 2), h_half - int(img12.get_height() / 2)))
######crash##########
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
#####################
    surface.blit(img, (0, 0))
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    pygame.draw.line(surface, 'black', (w_half, h_half), get_clock_pos_seconds(clock60, second), 7)
    get_clock_pos_hour(clock60, hour, 'hour')
    get_clock_pos_minute(clock60, minute, 'min')

###############TEXT##################TEXT##########TEXT###############
    basicFontForText = pygame.font.SysFont(None, 30)
    text = basicFontForText.render('B Azamat', True, 'grey', 'white')
    surface.blit(text, (0,0))
########################################################################
    pygame.display.flip()
    clock.tick(60)
