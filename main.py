import pygame
import random
from entities import *

pygame.init()
screenHight = 720
screenWidth = 1280
screen = pygame.display.set_mode((screenWidth,screenHight))
run = True


while run:
    pygame.display.set_caption(f'{player.frect}')
    # pygame.display.set_caption(str(pygame.display.get_current_refresh_rate()))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE]):
            run = False
    
    player.bounce2(player(10,20))
        
    screen.fill('black')
    
    for i in range(10):
        screen.blit(star.img,(random.randint(0,1250),random.randint(0,700)))

    screen.blit(player.img,player.frect)
    pygame.display.update()
    

pygame.quit()