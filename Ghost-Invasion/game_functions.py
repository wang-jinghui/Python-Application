# 集中存放管理事件的代码
import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, game_sets, screen, gun, bullets):
    if event.key == pygame.K_LEFT:
        gun.moving_left = True
    if event.key == pygame.K_RIGHT:
        gun.moving_right = True
    if event.key == pygame.K_UP:
        gun.moving_up = True
    if event.key == pygame.K_DOWN:
        gun.moving_down = True
    if event.key == pygame.K_SPACE:
        # ########################################
        new_bullet = Bullet(game_sets, screen, gun)
        bullets.add(new_bullet)

def check_keyup_events(event, gun):
    if event.key == pygame.K_LEFT:
        gun.moving_left = False
    if event.key == pygame.K_RIGHT:
        gun.moving_right = False
    if event.key == pygame.K_UP:
        gun.moving_up = False
    if event.key == pygame.K_DOWN:
        gun.moving_down = False

def check_events(game_sets, screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
             check_keydown_events(event, game_sets, screen, gun, bullets)

        elif event.type == pygame.KEYUP:
             check_keyup_events(event, gun)



# update screen
def update_screen(game_sets, screen, gun, bullets):
    screen.fill(game_sets.bg_color)  # 每次循环用背景色填充屏幕

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 在填充背景后绘制gun,确保它出现在背景前面
    gun.blitme()

    pygame.display.flip()  # 刷新屏幕，更新元素的位置

