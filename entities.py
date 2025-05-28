import pygame

screenHight = 720
screenWidth = 1280
screen = pygame.display.set_mode((screenWidth,screenHight))
rb = 1

class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    
    img = pygame.image.load('images/player.png').convert_alpha()
    frect = img.get_frect(center = (screenWidth/2,screenHight/2))
    #frect = img.get_frect(center = ()))
    x_pos = 0
    y_pos = 0    

    def bounce1(self):
        global rb
        if player.frect.right <screenWidth and not rb:
            player.frect.left+=1
            # print(player.frect.right)
            if player.frect.right==screenWidth:
                rb = 1
        if player.frect.left >0 and rb:
            player.frect.right-=1
            # print(player.frect.right)
            if player.frect.left==0:
                rb = 0
    
    def bounce2(self):
        global rb
        player.frect.x += rb * 1
        if player.frect.right>screenWidth or player.frect.left<0:
            rb*=-1

class star:
    img = pygame.image.load('images/star.png').convert_alpha()
    # for i in range(20):
    #     x_pos = random.randint(0,1250)
    #     y_pos = random.randint(0,700)

# import main