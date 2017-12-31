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
        # 在center_x 中存储小数
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        # 移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        # 根据self.rect的位置,绘制图像
        self.screen.blit(self.image, self.rect)


    def update(self, game_sets, screen):

        if self.moving_up and self.rect.bottom - 107 > 0:
            self.center_y -= game_sets.moving_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += game_sets.moving_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += game_sets.moving_speed

        if self.moving_left and self.rect.left > 0:
            self.center_x -= game_sets.moving_speed




        # 更新rect.centerx
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y
