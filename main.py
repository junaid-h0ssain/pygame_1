import pygame
import random
from entities import *
from actions import shoot

pygame.init()
clock = pygame.time.Clock()
run = True
p1 = player(100,100)
# l1 = laser()

sposx = []
sposy = []
for i in range(20):
    sposx.append(random.randint(0,1250))
    sposy.append(random.randint(0,700))

while run:
    clock.tick(60)
    pygame.display.set_caption(f'{pygame.time.Clock.get_fps(clock)}')
    # pygame.display.set_caption(str(pygame.display.get_current_refresh_rate()))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE]):
            run = False
    
    if keys[pygame.K_w] and p1.frect.top>0:
        p1.frect.centery-= p1.speed*.1
    if keys[pygame.K_s] and p1.frect.bottom<screenHight:
        p1.frect.centery+= p1.speed*.1
    if keys[pygame.K_d] and p1.frect.right<screenWidth:
        p1.frect.centerx+= p1.speed*.1
    if keys[pygame.K_a] and p1.frect.left>0:
        p1.frect.centerx-= p1.speed*.1
    
    #p1.bounce2()
        
    screen.fill('black')
    
    for i in range(20):
        # screen.blit(star.img,(random.randint(0,1250),random.randint(0,700)))
        screen.blit(star.img,(sposx[i],sposy[i]))


    screen.blit(p1.img,p1.frect)
    shoot(p1.frect.centerx,p1.frect.centery-64)
    
    
            
    pygame.display.update()
    

pygame.quit()