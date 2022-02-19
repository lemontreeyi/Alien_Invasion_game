import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from aliens import Alien
from game_stats import GameStats


class AlienInvasion:
    # 创建管理游戏资源&行为的类

    def __init__(self):
        # 写构造函数
        pygame.init()  # 初始化背景设置
        self.settings = Settings()

        # display.<> 返回surface对象，属于屏幕的一部分
        # 设置窗口大小，单位为像素
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)  # 创建飞船对象

        self.bullets = pygame.sprite.Group()  # 创建编组存储子弹
        self.aliens = pygame.sprite.Group()  # 创建编组存储外星人
        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 监视键盘&鼠标事件
            self._check_events()
            self._update_screen()
            self._update_bullet()
            self._update_aliens()
            self.ship.update()

    def _check_events(self):
        # event.get() 返回自上一次被调用后，发生事件组成的列表
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 单击窗口关闭键时，产生退出事件，通过sys.exit()退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)

    def _update_screen(self):
        # 每次循环结束后，重绘制屏幕，对surface对象fill方法填充颜色
        self.screen.fill(self.settings.bg_color)
        # 调用blitme方法绘制飞船
        self.ship.blitme()
        # 显示子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 显示外星人
        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        # 每次循环结束后，通过display.filp()隐藏旧屏幕，显示新屏幕，从而动态更新

    def _check_events_keydown(self, event):
        # 响应按键按下
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_events_keyup(self, event):
        # 响应按键弹起
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _fire_bullet(self):
        # 当子弹总数小于限制时,创建一颗子弹，并将其保存到bullets编组中
        if len(self.bullets) <= self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        # 控制刷新屏幕中的子弹
        self.bullets.update()
        # 删除飞出屏幕的子弹，避免浪费内存
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_fleet_bullet_collisions()

    def _check_fleet_bullet_collisions(self):
        # 检查是否有子弹击中外星人，若击中，则删除相应子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # 删除现有子弹&新建一群外星人
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        # 创建外星人舰队

        # 创建一个外星人并计算每行的容纳个数
        alien = Alien(self)
        ailen_width, alien_height = alien.rect.size
        space_x = self.settings.screen_width - (2 * ailen_width)
        alien_num_x = 5
        alien_num_y = 3

        for alien_numy in range(alien_num_y):
            for alien_numx in range(alien_num_x):
                self._create_alien(alien_numx, alien_numy)

    def _create_alien(self, alien_num_x, alien_num_y):
        # 创建一个外星人并将其放在当前行
        alien = Alien(self)
        ailen_width, alien_height = alien.rect.size
        alien.x = ailen_width + 2 * ailen_width * alien_num_x
        alien.y = 2 * alien_height * (2 / 3) * alien_num_y
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        # 外星人到达边缘时采取相应措施
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_dir()
                break

    def _change_fleet_dir(self):
        # 将外星人下移并改变他们的方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_dir *= -1

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人与飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("Ship hit!!!")
            self._ship_hit()

    def _ship_hit(self):
        # 相应飞船被外星人撞到
        self.stats.ships_left -= 1
        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        sleep(1)

    def _check_alien_bottom(self):
        # 检查是否有外星人到达底部
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


def main():
    game = AlienInvasion()
    game.run_game()


if __name__ == "__main__":
    main()
