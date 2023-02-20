import json

class GameStats():
    """Отслеживание статистики игры"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        #запуск игры в активном состоянии
        self.game_active = False

        #рекорды
        self.high_score = 0

        filename = 'D:\IT_Learning_Folder\Practice\Projects\Alien_Invasion\high_score.json'
        try:
            with open(filename) as f_obj:
                self.high_score = json.load(f_obj)
        except FileNotFoundError:
            self.high_score = 0
    
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1