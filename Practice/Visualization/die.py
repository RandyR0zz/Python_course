from random import randint

class Die():
    """Класс, представляющий кубик"""

    def __init__(self, num_sides=6):
        """Шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число"""
        return randint(1, self.num_sides)
        