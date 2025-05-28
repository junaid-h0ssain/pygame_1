import pygame
from entities import *

pygame.init()
screenHight = 720
screenWidth = 1280
screen = pygame.display.set_mode((screenWidth,screenHight))
run = True

while run:
    # pygame.display.set_caption(f'{player.x_pos}, {player.y_pos}')
    pygame.display.set_caption(str(pygame.display.get_current_refresh_rate()))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE]):
            run = False
    
    screen.fill('black')
    screen.blit(player.img,(player.x_pos,player.y_pos))
    for i in range(10):
        screen.blit(star.img,(random.randint(0,1250),random.randint(0,700)))
    pygame.display.update()

pygame.quit()