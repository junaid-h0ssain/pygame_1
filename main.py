import pygame

pygame.init()
screenHight = 720
screenWidth = 1280
screen = pygame.display.set_mode((screenWidth,screenHight))
run = True

while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE]):
            run = False
    
    pygame.display.update()

pygame.quit()