'''
pygame F11 --全屏
'''
import sys
import pygame
from pygame.locals import *

pygame.init()

Full_Screen = pygame.display.list_modes()[0]
Normal_Screen = 800,600

screen = pygame.display.set_mode( Normal_Screen )

bg = White_color = 255,255,255

turtle = pygame.image.load('turtle.png')

position = turtle.get_rect()
speed = [1,1]

screen_width, screen_height = screen.get_width(), screen.get_height() #获取屏幕的宽度和高度

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    position = position.move(speed)

    if position.left<0 or position.right>screen_width:
        speed[0] = -speed[0] #X轴
    if position.top<0 or position.bottom > screen_height:
        speed[1] = -speed[1] #Y轴
        
    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()

    pygame.time.delay(10) #延时 10毫秒,每秒刷新 1000/500 =200次,即:200帧

