from random import choice
# pylint: disable=no-member

class RandomWalk():
    # Класс для генерирования случайных блужданий
    
    def __init__(self, num_points=50000):
        # инициализирует атрибуты блуждания
        self.num_points = num_points

        # все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        # вычисляет все точки блуждания
        # шаги генерируются до достижения нужной длины
        while len(self.x_values) < self.num_points:
            # определение направления и длины перемещения
            x_step = self.get_step()
            y_step = self.get_step()

            # отклонение от нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # вычисление следующих значений x и y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            
    def get_step(self):
        # определяет длину и направление каждого шага
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance