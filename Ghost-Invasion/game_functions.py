# 集中存放管理事件的代码
import sys

import pygame

from bullet import Bullet
from ghost import Ghost

def check_keydown_events(event, game_sets, screen, gun, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_LEFT:
        gun.moving_left = True
    if event.key == pygame.K_RIGHT:
        gun.moving_right = True
    if event.key == pygame.K_UP:
        gun.moving_up = True
    if event.key == pygame.K_DOWN:
        gun.moving_down = True
    if event.key == pygame.K_SPACE:
        # 只有当前屏幕上子弹的数量小于,限制数量时才能发射新子弹
        fire_bullet(game_sets, screen, gun, bullets)



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
def update_screen(game_sets, screen, gun, bullets, ghosts):
    screen.fill(game_sets.bg_color)  # 每次循环用背景色填充屏幕

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 在填充背景后绘制gun,确保它出现在背景前面
    gun.blitme()
    # draw ghosts 对编组使用draw()会自动绘制编组的每个元素
    ghosts.draw(screen)
    pygame.display.flip()   # 刷新屏幕，更新元素的位置


def check_bullets(bullets, ghosts, game_sets, screen, gun):
    # 更新子弹位置
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检测碰撞,删除碰撞的子弹和ghost
    # sprite.groupcollide()检测bullet.rect 和　ghost.rect 之间的碰撞
    # collisions是一个字典对象,key:bullet,value:ghost
    # True,True 每个子弹击中ghost后消失
    # False, True 子弹到达屏幕顶端后消失
    collisions = pygame.sprite.groupcollide(bullets, ghosts, True, True)
    if len(ghosts) == 0:
        bullets.empty()
        create_fleet(game_sets, screen, ghosts, gun)


# fire
def fire_bullet(game_sets, screen, gun, bullets):
    if len(bullets) < game_sets.bullet_limit:
        new_bullet = Bullet(game_sets, screen, gun)
        bullets.add(new_bullet)

# 列数
def get_number_x(game_sets, ghost_width):
    available_space_x = game_sets.screen_width - 2 * ghost_width
    number_ghosts_x = int(available_space_x / (2 * ghost_width))
    return number_ghosts_x
# 行数
def get_number_y(game_sets, ghost_height, gun_height):
    available_space_y = game_sets.screen_height - 2* ghost_height - gun_height
    number_ghosts_y = int(available_space_y / (2 * ghost_height))
    return number_ghosts_y

def create_ghosts(game_sets, screen, ghost_width,
                  ghost_height,ghosts, number, row_number):
    ghost = Ghost(game_sets, screen)
    ghost.x = ghost_width + 2*ghost_width*number
    ghost.rect.x = ghost.x
    ghost.rect.y = ghost_height + 2 * ghost_height * row_number
    ghosts.add(ghost)


def create_fleet(game_sets, screen, ghosts, gun):
    ghost = Ghost(game_sets, screen)
    ghost_width = ghost.rect.width
    ghost_height = ghost.rect.height
    gun_height = gun.rect.height
    # 屏幕能容纳ghost数量
    number_ghosts_x = get_number_x(game_sets, ghost_width)
    number_ghosts_y = get_number_y(game_sets, ghost_height, gun_height)

    for row_number in range(number_ghosts_y):
        for number in range(number_ghosts_x):

             create_ghosts(game_sets, screen, ghost_width,
                           ghost_height,ghosts, number,row_number)

def update_ghost(game_sets, ghosts):
    check_fleet_edges(game_sets, ghosts)
    ghosts.update()

def check_fleet_edges(game_sets, ghosts):
    for ghost in ghosts.sprites():
        if ghost.check_edges():
            change_moving_direction(game_sets, ghosts)
            break

def change_moving_direction(game_sets, ghosts):
    for ghost in ghosts.sprites():
        ghost.rect.y += game_sets.ghost_drop_speed
    game_sets.moving_direction *= -1
