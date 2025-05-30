import pygame

screenHight = 720
screenWidth = 1280
screen = pygame.display.set_mode((screenWidth,screenHight))

class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('assets/images/player.png').convert_alpha()
        self.frect = self.img.get_frect(center = (x,y))
        self.rb = 1
        self.speed = 500
        self.directionx = pygame.math.Vector2(1,0)
        self.directiony = pygame.math.Vector2(0,1)   

    def bounce1(self):
        if self.frect.right <screenWidth and not self.rb:
            self.frect.left+=1
            if self.frect.right==screenWidth:
                self.rb = 1
        if self.frect.left >0 and self.rb:
            self.frect.right-=1
            if self.frect.left==0:
                self.rb = 0
    
    def bounce2(self,dt):
        self.frect.center += self.rb * self.speed*self.directionx*dt
        self.frect.center += self.rb * self.speed*self.directionx*dt
        if self.frect.right>screenWidth or self.frect.left<0:
            #self.frect.right=screenWidth
            # self.rb*=-1
            self.directionx.x*=-1
        if self.frect.bottom>screenHight or self.frect.top<0:
            #self.frect.right=screenHight
            # self.rb*=-1
            self.directionx.y*=-1
    
    def movement(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.frect.top>0:
            self.frect.center-= self.speed*self.directiony*dt
        if keys[pygame.K_s] and self.frect.bottom<screenHight:
            self.frect.center+= self.speed*self.directiony*dt
        if keys[pygame.K_d] and self.frect.right<screenWidth:
            self.frect.center+= self.speed*self.directionx*dt
        if keys[pygame.K_a] and self.frect.left>0:
            self.frect.center-= self.speed*self.directionx*dt

class star:
    img = pygame.image.load('assets/images/star.png').convert_alpha()

class laser:
    def __init__(self,x,y) -> None:
        self.img = pygame.image.load('assets/images/laser.png').convert_alpha()
        self.frect = self.img.get_frect(center = (x,y))