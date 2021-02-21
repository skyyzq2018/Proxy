from pygame.locals import *
from random import *
import pygame
import math
import sys

class Ball(pygame.sprite.Sprite) :  #继承动画精灵基类
    def __init__ (self,imgae,position,speed,bg_size) :
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imgae).convert_alpha()   
        self.rect = self.image.get_rect()   #获得球的尺寸
        self.rect.left , self.rect.top = position   #将出现的位置赋给球
        self.speed = speed  #设置速度
        self.width , self.height = bg_size[0] , bg_size[1]  #获得活动边界，就是背景的边界

    def move(self):
        self.rect = self.rect.move(self.speed)  #根据自身的速度进行移动

        if self.rect.right < 0:    #图片的右边已经超出边界的左边，即整个球已经出界
            self.rect.left = self.width    #让他从右边界回来
        if self.rect.bottom < 0:    #图片的底已经超出边界的上面
            self.rect.top = self.height   #让他从底部回来
        if self.rect.left > self.width:   #图片的左边已经超出边界的右边
            self.rect.right = 0     #让他从左边回来
        if self.rect.top > self.height:  #如果图片的顶部已经超出边界的底部
            self.rect.bottom = 0    #让他从顶部回来

#判断碰撞检测函数
def collide_check(item,target):
    col_balls = []      #添加碰撞小球
    for each in target:     #对 target 中所有的目标小球进行检测
        #两个球心之间的距离
        distance = math.sqrt( math.pow( (item.rect.center[0] - each.rect.center[0]) , 2 )  + \
                                        math.pow( (item.rect.center[1] - each.rect.center[1]) , 2) )
        if distance <= ( item.rect.width + each.rect.width ) / 2:   #如果距离小于等于两者间的半径之和也就是两个直径之和的一半
            col_balls.append(each)  #将这个发生碰撞的小球添加到列表中
    
    return col_balls


def main() :
    pygame.init()

    bg_image = r"D:\Code\Python\Pygame\pygame6：动画精灵\background.png"
    ball_image = r"D:\Code\Python\Pygame\pygame6：动画精灵\gray_ball.png" 
    
    running = True  #为了以后而已有多种方法退出程序
    
    bg_size = width , height = 1024 , 681       #背景大小
    screen = pygame.display.set_mode(bg_size) # 设置背景大小
    background = pygame.image.load(bg_image).convert_alpha()       #画背景

    balls = []

    # 创建五个小球
    BALL_NUM = 5

    for i in range (BALL_NUM) :    #生成5个球
        position = randint (0,width-100) ,  randint(0,height-100)   #要减去100是因为球图片尺寸的大小为100，随机生成位置
        speed  = [ randint (-10,10) , randint(-10,10) ]
        ball  = Ball(ball_image,position,speed,bg_size)  #生成球的对象
        balls.append(ball)  #将所有的球对象添加到类表中，方便管理
        
    clock = pygame.time.Clock()    #生成刷新帧率控制器

    while running :
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0, 0)) #将背景画到screen上

        for each in balls:  #每个球进行移动并重新绘制
            each.move()
            screen.blit(each.image, each.rect)
        
        for i in range (BALL_NUM) : #循环5个小球，分别判断这个小球有没有和另外四个小球发生碰撞
            item = balls.pop(i)    #因为是判断和其他四个小球，所以需要先将这个小球取出
            if collide_check( item , balls ):  #调用碰撞检测的函数，如果结果为真，也就是有发生碰撞的小球
                item.speed[0] = - item.speed[0]     #碰撞后向反方向运动
                item.speed[1] = - item.speed[1]
            balls.insert(i , item)  #最后不要忘记把这个小球放回原位

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
