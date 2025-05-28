import pygame
import random

pygame.init()
class player:
    img = pygame.image.load('images/player.png')#.convert_alpha()
    x_pos = 0
    y_pos = 100

class star:
    img = pygame.image.load('images/star.png')#.convert_alpha()
    # for i in range(20):
    #     x_pos = random.randint(0,1250)
    #     y_pos = random.randint(0,700)