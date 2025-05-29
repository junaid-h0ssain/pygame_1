import pygame
import random
from entities import *

def shoot(x,y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        l1 = laser(x,y)
        while l1.frect.centery>-20:
            screen.blit(l1.img,l1.frect)
            l1.frect.centery-=.1