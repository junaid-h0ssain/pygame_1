import pygame

screenHight = 720
screenWidth = 1280
screen = pygame.display.set_mode((screenWidth,screenHight))


class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('images/player.png').convert_alpha()
        # frect = img.get_frect(center = (screenWidth/2,screenHight/2))
        self.frect = self.img.get_frect(center = (x,y))
        self.rb = 1
        # x_pos = 0
        # y_pos = 0    

    def bounce1(self):
        
        if self.frect.right <screenWidth and not self.rb:
            self.frect.left+=1
            # print(player.frect.right)
            if self.frect.right==screenWidth:
                self.rb = 1
        if self.frect.left >0 and self.rb:
            self.frect.right-=1
            # print(player.frect.right)
            if self.frect.left==0:
                self.rb = 0
    
    def bounce2(self):
        
        self.frect.x += self.rb * 1
        if self.frect.right>screenWidth or self.frect.left<0:
            self.rb*=-1

class star:
    img = pygame.image.load('images/star.png').convert_alpha()
    # for i in range(20):
    #     x_pos = random.randint(0,1250)
    #     y_pos = random.randint(0,700)

# import main