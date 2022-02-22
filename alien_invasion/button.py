import pygame.font


class Button():
    def __init__(self, ai_game, msg):
        # инициализирует атрибуты кнопки
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_outline = self.screen.get_rect()
        self.lives = 3

        # назначение размеров и свойств кнопок
        self.width, self.height = 200, 50
        self.width_lose, self.height_lose = 250, 100
        self.button_color_lose = (100, 100, 0)
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.text_color_lose = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # построение объекта rect кнопки и выравнивание по центру экрана
        self.rect_lose = pygame.Rect(0, 0, self.width, self.height)
        self.rect_outline = pygame.Rect(0, 0, self.width+6, self.height+6)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect_lose.centerx = self.screen_rect.centerx
        self.rect_lose.top = self.screen_rect.top + 100

        self.rect_outline.center = self.screen_rect.center
        self.rect.center = self.screen_rect.center

        # сообщение кнопки создаётся только один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # преобразует msg в прямоугольник и выравнивает текст по центру
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def not_draw_button(self):
        pass

    def draw_button(self):
        # отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.text_color, self.rect_outline)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        if not self.lives:
            self.msg_lose_image = self.font.render("YOU DIED", True, self.text_color_lose,
                                            self.button_color_lose)
            self.msg_lose_image_rect = self.msg_lose_image.get_rect()
            self.msg_lose_image_rect.center = self.rect_lose.center
            self.screen.fill(self.button_color_lose, self.rect_lose)
            self.screen.blit(self.msg_lose_image, self.msg_lose_image_rect)
