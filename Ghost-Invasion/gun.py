import pygame


class Gun():

    def __init__(self, screen):
        # 初始化初始位置
        self.screen = screen

        # 加载图像，获取外接矩形
        self.image = pygame.image.load('images/pao1.bmp')
        self.rect = self.image.get_rect()
        # 游戏活动窗口的矩形  self.screen.get_rect()
        self.screen_rect = screen.get_rect()

        # 设置初始位置,屏幕的底部中央位置
        # pygame 中原点(0, 0)在屏幕的左上角
        # 元素居中,对应rect属性centerx,centery,center
        # 元素与屏幕边缘对齐,top,bottom,left,right
        # 元素水平垂直方向的位置x,y
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom


    def blitme(self):
        # 根据self.rect的位置,绘制图像
        self.screen.blit(self.image, self.rect)