class Settings():


    def __init__(self):
        # 屏幕设置参数
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.moving_speed = 2.0
        # 子弹
        self.bullet_speed = 2
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3    # 出现在屏幕上子弹的数量
        # ghost
        self.ghost_speed = 1
        self.ghost_drop_speed = 10
        self.moving_direction = 1
