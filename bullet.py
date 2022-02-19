import pygame
from pygame.sprite import Sprite
from settings import Settings


class Bullet(Sprite):
    """管理飞船发射的子弹类，继承自Sprite """
    
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # 先在原点创建一个子弹，再设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # 保存用浮点数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)