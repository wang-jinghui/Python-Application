
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
    ghosts = Group()
    gf.create_fleet(game_sets, screen, ghosts, gun)

    # 游戏主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(game_sets, screen, gun, bullets)
        # 更新炮的位置
        gun.update(game_sets, screen)


        # 更新子弹的位置
        # 删除消失的子弹
        gf.check_bullets(bullets, ghosts, screen, gun, game_sets)

        gf.update_ghost(game_sets,ghosts)
        # update screen
        gf.update_screen(game_sets, screen, gun, bullets, ghosts)


run_game()

