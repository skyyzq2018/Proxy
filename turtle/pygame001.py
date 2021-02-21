import sys,os
import pygame
from pygame.locals import *
from time import sleep
pygame.init()
#print(pygame.display.list_modes())

size = w,h = 800,600
bg = (255,255,255) # black
fg = (255,250,0  ) # king color

fullscreen = False

screen = pygame.display.set_mode(size,RESIZABLE)

pygame.display.set_caption("游戏: 乌龟行走 Turtle Walking")

turtle = pygame.image.load("turtle.png")

position= turtle.get_rect()
print(position)
speed = [-2,1]
r_head = pygame.transform.flip(turtle,True,False)
l_head = turtle
ratio =1
oturtle = turtle
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = r_head
                speed = [-1,0]
            if event.key == K_RIGHT:
                turtle = l_head
                speed = [1,0]
            if event.key == K_UP:
                turtle = r_head
                speed = [0,-1]
            if event.key == K_DOWN:
                turtle = l_head
                speed = [0,1]
            if event.key == K_EQUALS or event.key ==  K_MINUS or event.key == K_SPACE:
                
                if event.key == K_EQUALS and ratio < 2:
                   ratio +=0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1
                turtle = pygame.transform.smoothscale(oturtle,(int(w*ratio),int(h*ratio)))
                        
         #turtle move 移动
    position = position.move(speed)
    #pos=position
    if position.left <0 or position.right >w:
        turtle = r_head
        turtle = pygame.transform.flip(turtle,True,False)
        speed[0] = -speed[0]
    if position.top <0 or position.bottom >h:
        
        turtle = pygame.transform.flip(turtle,True,False)
        speed[1] = -speed[1]

    sleep(0.01)
    screen.fill(fg)
    screen.blit(turtle,position)
    #pygame.display.flip()
    pygame.display.update()

# while
        
