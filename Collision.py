# Collision_In_2-Dimension
import time
import pygame
import random
from os import system
frameRate = 200
collisions = []
dt = 1/200
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
        self.stop = None
    
    def display(self):
        try:
            pygame.draw.circle(screen, self.color, (round(self.center[0]),round(self.center[1])), self.radius)
        except:
            print(self.color)
    
    def update(self, dt):
        if abs(self.x) > 10000:
            self.x = (abs(self.x)/(self.x))*1000
        if abs(self.y) > 10000:
            self.y = (abs(self.y)/(self.y))*1000
        if self.stop != True:
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
            if self.stop == False:
                self.stop = None
        else:
            self.stop = False
            

    def friction(self, gravity, mu):
        pass
    
    def collision(self, group:list, collisions:list, dt):
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

                            # self.color = [abs(self.color[0]-i.color[0]), abs(self.color[1]-i.color[1]), abs(self.color[2]-i.color[2])]
                            # i.color = [abs(i.color[0]-self.color[0]), abs(i.color[1]-self.color[1]), abs(i.color[2]-self.color[2])]

                            self.update(dt *2)
                            i.update(dt *2)

                            if self.stop == None:
                                self.stop = True
                            if i.stop == None:
                                i.stop = True
                                
                            
                            # Resolving the ball stucking within each other issue from line 85-101, or next 17 lines...
                            dist = distance(i.center, self.center)
                            if dist < i.radius + self.radius:
                                if i.center[0]-self.center[0] == 0:
                                    i.center[1] += sign(i.center[1] - self.center[1]) * abs(i.radius+self.radius-dist)/2
                                    self.center[1] += sign(self.center[1] - i.center[1]) * abs(i.radius+self.radius-dist)/2
                                elif i.center[1]-self.center[1] == 0:
                                    i.center[0] += sign(i.center[0] - self.center[0]) * abs(i.radius+self.radius-dist)/2
                                    self.center[0] += sign(self.center[0] - i.center[0]) * abs(i.radius+self.radius-dist)/2
                                else:
                                    pass
                                    incHyp = (i.radius+self.radius-dist)/2
                                    incx = (incHyp/dist)*(abs(i.center[0] - self.center[0]))
                                    incy = (incHyp/dist)*(abs(i.center[1] - self.center[1]))
                                    i.center[0] += -incx* sign(i.center[0] - self.center[0])
                                    self.center[0] += -incx* sign(self.center[0] - i.center[0])
                                    i.center[1] += -incy *sign(i.center[0] - self.center[0])
                                    self.center[1] += -incy *sign(self.center[0] - i.center[0])
                            return [[self.number, i.number], [i.number, self.number]]
        return []

def sign(num):
    return 1 if num > 0 else -1

def exchange_vel(ivel1, ivel2, m1, m2, e1, e2):
    fvel1 = (1/(m1+m2))*((ivel1*(m1-e1*m2)) + (ivel2*(1+e1)*m2))
    fvel2 = (1/(m1+m2))*((ivel2*(m2-e2*m1)) + (ivel1*(1+e2)*m1))
    return [fvel1,fvel2]
                

def distance(point1,point2):
    return (((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))**0.5


if __name__ == '__main__':
    balls = []
    for i in range(100):
        balls.append(obj(10+int(random.random()*30), (40 + int(random.random()*600),40 + int(random.random()*600)), 20, (int(random.random()*200)+56,int(random.random()*200)+56,int(random.random()*200)+56), 0, int((0.5-random.random())*500), int((0.5-random.random())*500), 1, i))
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

        #code
        screen.fill((150,150,150))
        for i in balls:
            collisions.extend(i.collision([objs for objs in balls if objs.number != i.number], collisions, dt))
            i.update(dt)
            i.display()
        pygame.display.update()
        endTime = time.time()
        dt = endTime-initTime
        initTime = endTime
        if dt != 0: frameRate = 1/dt
        else: frameRate = 1000
