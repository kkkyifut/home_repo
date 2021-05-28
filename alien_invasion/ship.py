import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # Класс для управления кораблём
    def __init__(self, ai_game):
        # инициализирует корабль и задаёт его начальную позицию
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load(r'D:/study/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # каждый новый корабль появляется у нижнего края
        self.rect.midbottom = self.screen_rect.midbottom

        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # обновляет позицию корабля с учётом флага
        # обновляется атрибут x, не rect
        self.image = pygame.image.load(r'D:/study/alien_invasion/images/ship.bmp')
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.image = pygame.image.load(r'D:/study/alien_invasion/images/ship_right.bmp')
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.image = pygame.image.load(r'D:/study/alien_invasion/images/ship_left.bmp')
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            self.image = pygame.image.load(r'D:/study/alien_invasion/images/ship.bmp')
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            self.image = pygame.image.load(r'D:/study/alien_invasion/images/ship_down.bmp')
        # обновление атрибута rect на основании self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # размещает корабль в центре нижней стороны
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)