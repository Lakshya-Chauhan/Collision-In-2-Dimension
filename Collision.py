# Collision_In_2-Dimension
import time
import pygame
import random
from os import system
frameRate = 100
collisions = []
class obj:
    screen_size = [800, 800]
    def __init__(self, mass, center, radius, color = (0, 0, 0), acceleration = 0, velx = 0, vely = 0, e = 1, number = None):
        self.mass = mass
        self.center = list(center)
        self.radius = radius
        self.color = color
        self.x = velx
        self.y = vely
        self.a = acceleration
        self.e = e
        self.number = number
    
    def display(self):
        pygame.draw.circle(screen, self.color, (round(self.center[0]),round(self.center[1])), self.radius)
    
    def update(self, dt):
        if abs(self.x) > 10000:
            self.x = (abs(self.x)/(self.x))*1000
        if abs(self.y) > 10000:
            self.y = (abs(self.y)/(self.y))*1000
        self.center[0] += self.x *dt
        self.center[1] += self.y *dt
        if self.center[0] > obj.screen_size[0]-self.radius:
            self.center[0] -= 2*(self.center[0]-self.screen_size[0]+self.radius)
            self.x *= -1
        elif self.center[0] < self.radius:
            self.center[0] += 2*(self.radius-self.center[0])
            self.x *= -1

        if self.center[1] > obj.screen_size[1]-self.radius:
            self.center[1] -= 2*(self.center[1]-self.screen_size[1]+self.radius)
            self.y *= -1
        elif self.center[1] < self.radius:
            self.center[1] += 2*(self.radius-self.center[1])
            self.y *= -1
            

    def friction(self, gravity, mu):
        pass
    
    def collision(self, group:list, collisions:list):
        for i in group:
            if [self.number, i.number] not in collisions:
                if (i.center[0] - self.center[0]) <= i.radius + self.radius:
                    if (i.center[1] - self.center[1]) <= i.radius + self.radius:
                        if distance(i.center, self.center) <= i.radius + self.radius:
                            final_vels = [
                                exchange_vel(self.x, i.x, self.mass, i.mass, self.e, i.e),
                                exchange_vel(self.y, i.y, self.mass, i.mass, self.e, i.e)
                            ]
                            self.x, i.x = final_vels[0][0], final_vels[0][1]
                            self.y, i.y = final_vels[1][0], final_vels[1][1]
                            return [[self.number, i.number], [i.number, self.number]]
        return []

def exchange_vel(ivel1, ivel2, m1, m2, e1, e2):
    fvel1 = (1/(m1+m2))*((ivel1*(m1-e1*m2)) + (ivel2*(1+e1)*m2))
    fvel2 = (1/(m1+m2))*((ivel2*(m2-e2*m1)) + (ivel1*(1+e2)*m1))
    return [fvel1,fvel2]
                

def distance(point1,point2):
    return (((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))**0.5


if __name__ == '__main__':
    balls = [
        obj(20, (200,200), 50, (200,0,200), 0, 60*5, 60*5, 1, 0),
        obj(18, (300,300), 45, (0,200,200), 0, 60*5, 70*5, 1, 1),
        obj(16, (300,400), 40, (200,200,0), 0, 40*5, 70*5, 1, 2),
        obj(14, (300,600), 35, (200,0,0), 0, 90*5, 20*5, 1, 3),
        obj(12, (300,700), 30, (0,200,0), 0, 40*5, 80*5, 1, 4),
        obj(10, (400,400), 25, (0,0,200), 0, 70*5, 80*5, 1, 5)
    ]
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Collision")
    running = True
    initTime = time.time()
    clock = pygame.time.Clock()
    while running == True:
        collisions.clear()
        clock.tick(frameRate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        endTime = time.time()
        dt = endTime-initTime
        initTime = endTime
        if dt != 0: frameRate = 1/dt
        else: frameRate = 1000

        #code
        screen.fill((150,150,150))
        for i in balls:
            collisions.extend(i.collision([objs for objs in balls if objs.number != i.number], collisions))
            i.update(dt)
            i.display()
        pygame.display.update()
