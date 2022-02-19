import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 创建外星人类
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/alien.png").convert_alpha()
        self.rect = self.image.get_rect()

        # 设定外星人初始位置
        self.rect.x = 0
        self.rect.y = 0

        # 浮点数存储外星人的坐标位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # 移动外星人
        self.x += (self.settings.alien_speed * self.settings.fleet_dir)
        self.rect.x = self.x

    def check_edges(self):
        # 检测外星人是否撞到边缘
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
