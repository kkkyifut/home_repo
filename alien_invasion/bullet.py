import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # Класс для управления снарядами, выпущенными кораблём
    def __init__(self, ai_game):
        # создаёт объект снарядов в текущей позиции корабля
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # позиция снаряда хранится в вещественном формате
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # перемещает снаряд вверх по экрану
        # обновление позиции снаряда в вещественном формате
        # self.y -= self.settings.bullet_speed
        if self.moving_right == 1:
            self.x += self.settings.bullet_speed
        if self.moving_left == 2:
            self.x -= self.settings.bullet_speed
        if self.moving_up:
            self.y -= self.settings.bullet_speed
        if self.moving_down == 3:
            self.y += self.settings.bullet_speed

        # обновление позиции прямоугольника
        self.rect.y = self.y
        self.rect.x = self.x
            
    def draw_bullet(self):
        # выводит снаряд на экран
        pygame.draw.rect(self.screen, self.color, self.rect)