import pygame, const, math, physics
from const import *

class circle():
     
    def __init__(self, location, speed, radius=50, color=WHITE):
        self.color = color
        self.radius = radius
        self.x = location[0]
        self.y = location[1]
        self.xspeed = speed[0] 
        self.yspeed = speed[1] 

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    @property
    def right(self):
        return self.x + self.radius

    @right.setter
    def right(self, value):
        self.x = value - self.radius


    @property
    def left(self):
        return self.x - self.radius

    @left.setter
    def left(self, value):
        self.x = value + self.radius

    @property
    def top(self):
        return self.y - self.radius
    
    @top.setter
    def top(self, value):
        self.y = value + self.radius

    @property
    def bottom(self):
        return self.y + self.radius

    @bottom.setter
    def bottom(self, value):
        self.y = value - self.radius

    def _collision(self, objects):
        #FIXME
        # only support circles
        for i in objects:
            if i is not self:
                physics.collide_circle(self, i)

    def update(self, objects):

        self.x += self.xspeed
        self.y += self.yspeed
        self._boundary()
        self._collision(objects)
        
    def _boundary(self):
        if self.right >= WIDTH:
            self.right = WIDTH #- abs(self.xspeed)
            self.xspeed = -self.xspeed
            assert self.x == WIDTH - self.radius

        if self.left <= 0:
            self.left = 0 #+ abs(self.xspeed)
            self.xspeed = -self.xspeed
            assert self.x == 0 + self.radius

        if self.top <= 0:
            self.top = 0 #+ abs(self.yspeed)
            self.yspeed = -self.yspeed
            assert self.y == 0 + self.radius

        if self.bottom >= HEIGHT:
            self.bottom = HEIGHT #- abs(self.yspeed)
            self.yspeed = -self.yspeed
            assert self.y == HEIGHT - self.radius

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.radius, 0)
    
