
import pygame
from pygame.sprite import Group
from settings import Settings
from gun import Gun


import game_functions as gf


def run_game():
    pygame.init()  # 初始化背景
    game_sets = Settings()    # 设置类的实例
    # 创建一个游戏窗口，大小通过设置类的属性确定
    screen = pygame.display.set_mode((game_sets.screen_width,game_sets.screen_height))
    pygame.display.set_caption("Ghost Invasion")

    # gun
    gun = Gun(screen)

    # 子弹编组
    bullets = Group()
    # 游戏主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(game_sets, screen, gun, bullets)
        # 更新炮的位置
        gun.update(game_sets, screen)

        # 更新子弹的位置
        bullets.update()

        # update screen
        gf.update_screen(game_sets, screen, gun, bullets)


run_game()

