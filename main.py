import pygame
import random
from entities import *
from actions import shoot

pygame.init()
clock = pygame.time.Clock()
fps = 60
run = True
p1 = player(100,100)

sposx = []
sposy = []
for i in range(20):
    sposx.append(random.randint(0,1250))
    sposy.append(random.randint(0,700))

while run:
    dt = clock.tick(fps)/1000
    #print(dt)
    pygame.display.set_caption(f'{pygame.time.Clock.get_fps(clock)}')
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE]):
            run = False
    
    p1.movement(dt)
    # p1.bounce2(dt)
        
    screen.fill('black')
    
    for i in range(20):
        # screen.blit(star.img,(random.randint(0,1250),random.randint(0,700)))
        screen.blit(star.img,(sposx[i],sposy[i]))

    screen.blit(p1.img,p1.frect)
    shoot(p1.frect.centerx,p1.frect.centery-64)
           
    pygame.display.update()
    

pygame.quit()