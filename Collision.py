# Collision_In_2-Dimension
import pygame
import random
from os import system
system("cls")
mobj1 = int(input("Please Enter The Mass of Blue Ball : "))
mobj2 = int(input("Please Enter The Mass of Green Ball : "))
system("cls")
print("\n\n\nBelow Velocities after Collision are being printed:-\n")
bpos1 = (451,451)  #Position of First Ball(Blue)
bpos2 = (400,400)  #Position of Second Ball(Green)
xmovement1 = int((random.random())*10)+1     #component of vector speed of blue ball along x-axis
xmovement2 = int((random.random())*10)+1     #component of vector speed of green ball along x-axis
ymovement1 = int((random.random())*10)+1     #component of vector speed of blue ball along y-axis
ymovement2 = int((random.random())*10)+1     #component of vector speed of green ball along y-axis
center1 = 0      #Center of Blue Ball
center2 = 0      #Center of Green Ball
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Collision")
pygame.display.set_icon(icon)
BACK = pygame.transform.scale(pygame.image.load("ndark.jpg"),(800,800))
BALL1 = pygame.transform.scale(pygame.image.load("selected30.png"),(50,50))
BALL2 = pygame.transform.scale(pygame.image.load("selected31.png"),(50,50))
def ball1(x : float , y : float):
    global bpos1,center1
    bpos1 = (bpos1[0]+x,bpos1[1]+y)
    center1 = (bpos1[0]+25,bpos1[1]+25)
    screen.blit(BALL1,bpos1)
def ball2(x : float , y : float):
    global bpos2,center2
    bpos2 = (bpos2[0]+x,bpos2[1]+y)
    center2 = (bpos2[0]+25,bpos2[1]+25)
    screen.blit(BALL2,bpos2)
def back():
    screen.blit(BACK,(0,0))
running = True
clock = pygame.time.Clock()
while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if bpos1[0] not in range(0,750):
        xmovement1 = (-xmovement1)
    if bpos1[1] not in range(0,750):
        ymovement1 = (-ymovement1)
    if bpos2[0] not in range(0,750):
        xmovement2 = (-xmovement2)
    if bpos2[1] not in range(0,750):
        ymovement2 = (-ymovement2)
    back()
    ball1(xmovement1,ymovement1)
    ball2(xmovement2,ymovement2)
    if int((((center1[0]-center2[0])**2)+((center1[1]-center2[1])**2))**0.5) in range(0,51):                  #Checking if there is a collision
        xmovement1,xmovement2 = round(((xmovement1*((mobj1-mobj2)/(mobj1+mobj2))) + ((2*mobj2*xmovement2)/(mobj1+mobj2)))) ,round(((xmovement2*((mobj2-mobj1)/(mobj2+mobj1))) + ((2*mobj1*xmovement1)/(mobj1+mobj2))))
        ymovement1,ymovement2 = round(((ymovement1*((mobj1-mobj2)/(mobj1+mobj2))) + ((2*mobj2*ymovement2)/(mobj1+mobj2)))) ,round(((ymovement2*((mobj2-mobj1)/(mobj2+mobj1))) + ((2*mobj1*ymovement1)/(mobj1+mobj2))))
        print(f'''\n\n\n\tVelocity(Along x-axis) of Blue Ball : {xmovement1}
        Velocity(Along y-axis) of Blue Ball : {ymovement1}
        
        Velocity(Along x-axis) of Green Ball : {xmovement2}
        Velocity(Along y-axis) of Green Ball : {ymovement2}''')
    pygame.display.update()
