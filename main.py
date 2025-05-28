import pygame
import random
from entities import *

pygame.init()
screenHight = 720
screenWidth = 1280
screen = pygame.display.set_mode((screenWidth,screenHight))
run = True
p1 = player(100,100)
p2 = player(200,200)

while run:
    pygame.display.set_caption(f'{p1.frect}')
    # pygame.display.set_caption(str(pygame.display.get_current_refresh_rate()))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE]):
            run = False
    
    p1.bounce1()
    p2.bounce2()
        
    screen.fill('black')
    
    for i in range(10):
        screen.blit(star.img,(random.randint(0,1250),random.randint(0,700)))

    screen.blit(p1.img,p1.frect)
    screen.blit(p2.img,p2.frect)
    pygame.display.update()
    

pygame.quit()