import pygame

# 将游戏中的元素编组,进而同时操作组中的所以元素
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_sets, screen, gun):
        super().__init__()
        self.screen = screen
        # 创建子弹的rect,初始位置
        self.rect = pygame.Rect(0, 0, game_sets.bullet_width, game_sets.bullet_height)
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        # 子弹y坐标
        self.y = float(self.rect.y)
        self.color = game_sets.bullet_color
        self.speed = game_sets.bullet_speed

    def update(self):
        # 向上移动
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)