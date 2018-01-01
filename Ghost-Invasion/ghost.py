import pygame

from pygame.sprite import Sprite

class Ghost(Sprite):
    def __init__(self, game_sets, screen):
        super().__init__()
        self.screen = screen
        self.game_sets = game_sets
        # 加载ghost图像
        self.image = pygame.image.load('images/th.bmp')
        self.rect = self.image.get_rect()
        # 初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.game_sets.ghost_speed * self.game_sets.moving_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return  True
