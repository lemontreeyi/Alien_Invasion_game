import pygame
from settings import Settings


class Ship:
    # 创建管理飞船的类

    def __init__(self, ai_game):  # ai_game为AlienInvasion对象
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 将游戏窗体作为成员属性，方便后续使用

        # 加载飞船并获取其外接矩形
        self.image = pygame.image.load("images/ship.png").convert_alpha()  # 加载飞船图片
        self.rect = self.image.get_rect()

        # 将飞船放在屏幕底部
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        # 设置飞船的坐标属性，并转换为浮点数,方便记录
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
        elif self.moving_top and self.rect.top>350:
            self.y -= self.settings.ship_speed
        elif self.moving_bottom and self.rect.bottom<720:
            self.y += self.settings.ship_speed
        # 更新飞船的位置
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # 让飞船居中
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
