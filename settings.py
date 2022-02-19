class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (250, 250, 250)
        self.ship_speed = 0.6
        self.ship_limit = 3

        # 规定子弹的属性
        self.bullet_speed = 1.3
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 20

        # 设置外星人的属性
        self.alien_speed = 0.6
        self.fleet_drop_speed = 30
        # fleet_dir为1表示右移，为-1表示左移
        self.fleet_dir = 1


