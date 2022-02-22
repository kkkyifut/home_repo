class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        # инициализирует статические настройки игры
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_limit = 3

        # параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # настройки пришельцев
        self.fleet_drop_speed = 10

        # темп ускорения игры
        self.speedup_scale = 1.1
        # темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # инициализирует настройки, меняющиеся в ходе игры
        self.ship_speed = 1.0
        self.bullet_speed = 1.5
        self.alien_speed = 0.5

        # fleet_direction = 1 обозначает движение вправо, а -1 - налево
        self.fleet_direction = 1

        # подсчёт очков
        self.alien_points = 50

    def increase_speed(self):
        # увеличивает скорость игры
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
