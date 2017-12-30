
import pygame

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


    # 游戏主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events()


        screen.fill(game_sets.bg_color)    # 每次循环用背景色填充屏幕
        # 在填充背景后绘制gun,确保它出现在背景前面
        gun.blitme()


        pygame.display.flip()    # 刷新屏幕，更新元素的位置

run_game()

